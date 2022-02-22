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
            ghostImg = document.getElementById('ghost'),
            defaultMsg = document.getElementById('defaultMsg');

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

        // Game entities
        this.pickups = [];
        this.ghost = null;
        this.player = null;

        // Score variables
        this.pickupsRemaining = 0;
        this.playerScore = 0;
        this.scoreDisplay = document.getElementById('score');

        // Timestamp of the previously rendered frame
        this.prevFrame = 0;
        
        // Event listener for detecting input
        window.addEventListener('keydown', (e) => { this.handleInput(e); })

        // For each row in the logical arena map
        for (let tileY = 0; tileY < MAP_HEIGHT; tileY++) {
            let row = map[tileY];

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
                    this.ghost = new Ghost(tileX, tileY, ghostImg);
                }
            }
        }
    }

    /**
     * Handles keyboard input
     * 
     * @param {KeyboardEvent} e - The keyboard event being handled
     */
    handleInput(e) {
        // Don't repeatedly handle a held key
        if (!e.repeat) {
            // Queue the direction corresponding to the pressed key
            if (e.key == 'ArrowLeft') {
                this.player.queueDirection(LEFT);
            }
            else if (e.key == 'ArrowRight') {
                this.player.queueDirection(RIGHT);
            }
            else if (e.key == 'ArrowUp') {
                this.player.queueDirection(UP);
            }
            else if (e.key == 'ArrowDown') {
                this.player.queueDirection(DOWN);
            }
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

    winGame() {
        // To-Do
    }

    loseGame() {
        // To-Do
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
        requestAnimationFrame(() => { this.mainLoop(); });
    }

    /**
     * Updates the states of game entities
     * 
     * @param {number} elapsed - The elapsed time, in seconds, since the previous update
     */
    update(elapsed) {
        let tileContents;

        // Call individual entity update methods
        this.player.update(map, elapsed);
        this.ghost.update(map, elapsed, this.player.tileX, this.player.tileY);

        // Check if the player's current map tile contains a number (corresponding to a pickup in
        // the pickup array)
        tileContents = map[this.player.tileY][this.player.tileX];
        if (typeof tileContents === 'number') {
            let pickup = this.pickups[tileContents];

            // Update the player's score
            this.updateScore(pickup.value);

            // If this pickup is a power pill, make the ghost vulnerable
            if (pickup.type == 'p' && !this.ghost.resetting) {
                this.ghost.startBlue();
            }

            // Remove the pickup from the canvas and pickup array, and decrement pickupsRemaning
            pickup.remove(this.pickupCtx);
            this.pickups[tileContents] = null;
            this.pickupsRemaining--;

            // Remove the pickup reference from the tile map
            map[this.player.tileY][this.player.tileX] = 'o';

            // The player has won the game when there are no pickups remaining
            if (this.pickupsRemaining <= 0) {
                this.winGame();
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
                this.loseGame();
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

const test = new PacMan();
test.start();