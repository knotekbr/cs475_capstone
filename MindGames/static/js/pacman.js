import { map } from './map.js';
import { Pickup } from './entities/pickup.js';
import { Player } from './entities/player.js';
import { Ghost } from './entities/ghost.js';
import {
    MAP_WIDTH,
    MAP_HEIGHT,
    RIGHT,
    DOWN,
    LEFT,
    UP
} from './constants.js';

/**
 * Represents a Pac-Man game
 * @class
 */
class PacMan {

    /**
     * Instantiates a new PacMan object
     */
    constructor() {
        // DOM elements not needed outside of the constructor
        const
            container = document.getElementById('game'),
            defaultMsg = document.getElementById('default-msg');

        // Remove the default error message
        defaultMsg.remove();

        // Main canvas and associated drawing context for rendering dynamic entities
        this.cnv = document.getElementById('cnv');
        this.ctx = this.cnv.getContext('2d');
        // Main canvas dimensions
        this.width = this.cnv.width = container.clientWidth;
        this.height = this.cnv.height = container.clientHeight;

        // Pickup canvas and associated drawing context for rendering static pickup entities
        this.pickupCnv = document.getElementById('pickups');
        this.pickupCtx = this.pickupCnv.getContext('2d');
        // Pickup canvas dimensions
        this.pickupCnv.width = this.width;
        this.pickupCnv.height = this.height;

        // Ghost sprite sheet element
        this.ghostImg = document.getElementById('ghost');

        // UI player score element
        this.scoreDisplay = document.getElementById('score');

        //UI arrow elements and associated direction constants
        this.arrows = {
            ArrowLeft: {
                element: document.getElementById('left-arrow'),
                direction: LEFT
            },
            ArrowRight: {
                element: document.getElementById('right-arrow'),
                direction: RIGHT
            },
            ArrowUp: {
                element: document.getElementById('up-arrow'),
                direction: UP
            },
            ArrowDown: {
                element: document.getElementById('down-arrow'),
                direction: DOWN
            }
        };
        // Arrow element corresponding to last received direction input
        this.lastArrow = this.arrows.ArrowUp.element;

        // UI button elements
        this.toggleButton = document.getElementById('toggle-pause');
        this.newGameButton = document.getElementById('new-game');

        // Game over elements
        this.gameOverScreen = document.getElementById('game-over');
        this.winLoseMessage = document.getElementById('win-lose');
        this.finalScore = document.getElementById('final-score');

        // Timestamp of the previously rendered frame
        this.prevFrame = 0;

        // WebSocket connection for receiving commands from the server
        this.sock = new WebSocket('ws://' + location.host + '/obci');
        
        // Event listeners
        window.addEventListener('keydown', (e) => { this.handleInput(e); });
        this.toggleButton.addEventListener('click', () => { this.togglePause(); });
        this.newGameButton.addEventListener('click', () => { this.newGame(); });
        this.sock.addEventListener('message', (e) => { this.handleInput({repeat: false, key: e.data}) });

        // Initialize a new gameplay instance
        this.init();
    }

    /**
     * Sets all game entities, elements, and variables to their default states
     */
    init() {
        // Begin the game in a paused state
        this.paused = true;

        // Set UI elements to default states
        this.toggleButton.innerHTML = 'Start Game';
        this.toggleButton.disabled = false;
        this.gameOverScreen.classList.remove('visible');
        this.scoreDisplay.innerHTML = '00';
        this.lastArrow.classList.remove('last-arrow');

        // Clear all previous drawings from both canvases
        this.ctx.clearRect(0, 0, this.width, this.height);
        this.pickupCtx.clearRect(0, 0, this.width, this.height);

        // Game entities
        this.pickups = [];
        this.ghost = null;
        this.player = null;

        // Score variables
        this.pickupsRemaining = 0;
        this.playerScore = 0;

        // Local copy of logical game map
        this.map = [];
        for (let row = 0; row < MAP_HEIGHT; row++) {
            this.map.push([...map[row]]);
        }

        // For each row in the logical arena map
        for (let tileY = 0; tileY < MAP_HEIGHT; tileY++) {
            let row = this.map[tileY];

            // For each column in the current row
            for (let tileX = 0; tileX < MAP_WIDTH; tileX++) {
                // If the character at this position represents a pickup
                if (row[tileX] == 'c' || row[tileX] == 'p') {
                    let pickup = new Pickup(tileX, tileY, row[tileX]);

                    // Draw the pickup on the pickup canvas
                    pickup.draw(this.pickupCtx);
                    // Replace the map character with the index of this pickup in the pickups array
                    row[tileX] = this.pickups.length;
                    // Add this pickup to the pickups array and increment pickupsRemaining
                    this.pickups.push(pickup);
                    this.pickupsRemaining++;
                }
                // Else if the character at this position represents the player's starting position
                else if (row[tileX] == 's') {
                    this.player = new Player(tileX, tileY);
                }
                // Else if the character at this position represents the ghost's starting position
                else if (row[tileX] == 'g') {
                    this.ghost = new Ghost(tileX, tileY, this.ghostImg);
                }
            }
        }

        // Draw the game in its initial state
        this.draw();
    }

    /**
     * Toggles the paused state of the game
     */
    togglePause() {
        this.paused = !this.paused;

        if (this.paused) {
            // Cancel request for next iteration of mainLoop()
            cancelAnimationFrame(this.frameRequest);
            this.toggleButton.innerHTML = 'Resume';
        }
        else {
            // Start mainLoop()
            this.start();
            this.toggleButton.innerHTML = 'Pause';
        }
    }

    /**
     * Ends the current game and starts a new one
     */
    newGame() {
        cancelAnimationFrame(this.frameRequest);
        this.init();
    }

    /**
     * Handles keyboard input
     * 
     * @param {KeyboardEvent} e - The keyboard event being handled
     */
    handleInput(e) {
        // Only handle arrow keys that aren't being held down
        if (!e.repeat && e.key in this.arrows) {
            // Update UI elements to visually indicate the received direction
            this.lastArrow.classList.remove('last-arrow');
            this.lastArrow = this.arrows[e.key].element;
            this.lastArrow.classList.add('last-arrow');

            // Queue the received direction
            this.player.queueDirection(this.arrows[e.key].direction);
        }  
    }

    /**
     * Updates and displays the player's score
     * 
     * @param {number} value - The amount to add to the player's current score
     */
    updateScore(value) {
        this.playerScore += value;
        this.scoreDisplay.innerHTML = this.playerScore;
    }

    /**
     * Displays the game over screen
     * 
     * @param {string} message - Text to display in the form 'You <message>'
     */
    gameOver(message) {
        // Pause the game and disable the 'Resume' button
        this.toggleButton.disabled = true;
        this.togglePause();

        // Customize the game over screen and display it
        this.winLoseMessage.innerHTML = message;
        this.finalScore.innerHTML = this.playerScore;
        this.gameOverScreen.classList.add('visible');
    }

    /**
     * Starts the game by entering the main loop
     */
    start() {
        this.prevFrame = new Date();
        this.mainLoop();
    }

    /**
     * Main game loop for updating and drawing
     */
    mainLoop() {
        // Calculate the time elapsed since the last frame was rendered
        let
            currFrame = new Date(),
            elapsed = (currFrame - this.prevFrame) / 1000;

        // This frame is now the previous frame
        this.prevFrame = currFrame;
        
        // Update and draw
        this.update(elapsed);
        this.draw();

        // Request an animation frame for the next iteration of the game loop
        if (!this.paused) {
            this.frameRequest = requestAnimationFrame(() => { this.mainLoop(); });
        }
    }

    /**
     * Updates the states of game entities
     * 
     * @param {number} elapsed - The elapsed time, in seconds, since the previous update
     */
    update(elapsed) {
        let tileContents;

        // Call individual entity update methods
        this.player.update(this.map, elapsed);
        this.ghost.update(this.map, elapsed, this.player.tileX, this.player.tileY);

        // Check if the player's current map tile contains a number (corresponding to a pickup in
        // the pickup array)
        tileContents = this.map[this.player.tileY][this.player.tileX];
        if (typeof tileContents === 'number') {
            let pickup = this.pickups[tileContents];

            // Update the player's score
            this.updateScore(pickup.value);

            // If this pickup is a power pill, and the ghost is not resetting, make the ghost
            // vulnerable
            if (pickup.type == 'p' && !this.ghost.resetting) {
                this.ghost.startBlue();
            }

            // Remove the pickup from the canvas and pickup array, and decrement pickupsRemaning
            pickup.remove(this.pickupCtx);
            this.pickups[tileContents] = null;
            this.pickupsRemaining--;

            // Remove the pickup reference from the tile map
            this.map[this.player.tileY][this.player.tileX] = 'o';

            // The player has won the game when there are no pickups remaining
            if (this.pickupsRemaining <= 0) {
                this.gameOver('won!');
            }
        }

        // If the player and the ghost are on the same tile
        if (this.player.tileX == this.ghost.tileX && this.player.tileY == this.ghost.tileY) {
            // If the ghost is blue, the player earns points and the ghost resets
            if (this.ghost.blue) {
                this.updateScore(200);
                this.ghost.startReset();
            }
            // If the player encounters a ghost that is neither blue nor resetting, they lose the
            // game
            else if (!this.ghost.blue && !this.ghost.resetting) {
                this.gameOver('lost...');
            }
        }
    }

    /**
     * Draws game entities to the main canvas
     */
    draw() {
        // Clear canvas contents
        this.ctx.clearRect(0, 0, this.width, this.height);

        // Call individual entity draw methods
        this.player.draw(this.ctx);
        this.ghost.draw(this.ctx);
    }

}

const game = new PacMan();