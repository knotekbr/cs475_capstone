import { Mover } from './mover.js';
import {
    GHOST_SIZE,
    GHOST_SPEED,
    GHOST_FRAMES,
    GHOST_FPS,
    GHOST_BLUE_STATE,
    GHOST_FLASH_STATE,
    GHOST_RESET_STATE,
    GHOST_BLUE_DUR,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    GHOST_CHASE_WEIGHT
} from '../constants.js';

/**
 * Represents a ghost entity
 * @class
 */
export class Ghost extends Mover {

    /**
     * Instantiates a new Ghost object
     * 
     * @param {number} tileX - The tile map x coordinate of the ghost
     * @param {number} tileY - The tile map y coordinate of the ghost
     * @param {CanvasImageSource} spriteSheet - The image to be used as a sprite sheet
     */
    constructor(tileX, tileY, spriteSheet) {
        // Superclass constructor call
        super(tileX, tileY, false, GHOST_SIZE, GHOST_SPEED);

        this.spriteSheet = spriteSheet;
        this.drawOffset = GHOST_SIZE / 2;

        // Indicates which row of the sprite sheet to draw from
        this.baseState = this.direction;
        // The current animation frame
        this.aniState = 0;
        // The duration of an individual animation frame
        this.frameDur = 1 / GHOST_FPS;
        // Elapsed time since the previous animation frame
        this.prevFrame = 0;

        // Vulnerable (blue) state flag and associated timer
        this.blue = false;
        this.blueTimer = 0;

        // Resetting (after being eaten) flag and coordinates to reset to
        this.resetting = false;
        this.defaultX = tileX;
        this.defaultY = tileY;

        // References the current function being used to determine the next direction of movement.
        // Differs between default/vulnerable and reset states
        this.chooseDirection = this.defaultChooseDirection;
    }

    /**
     * Changes the ghost's movement direction to the queued direction
     */
    changeDirection() {
        // Superclass changeDirection() call
        super.changeDirection();

        // If the ghost is not blue, its base state is equal to its direction
        if (!this.blue && !this.resetting) {
            this.baseState = this.direction;
        }
    }

    /**
     * Transitions the ghost into its vulnerable state
     */
    startBlue() {
        this.blue = true;
        this.blueTimer = GHOST_BLUE_DUR;
        this.baseState = GHOST_BLUE_STATE;
    }

    /**
     * Transitions the ghost out of its vulnerable state
     */
    endBlue() {
        this.blue = false;
        this.baseState = this.direction;
    }

    /**
     * Transitions the ghost into its reset state
     */
    startReset() {
        // Can't be both blue and resetting
        this.blue = false;
        this.resetting = true;
        this.baseState = GHOST_RESET_STATE;
        this.chooseDirection = this.resettingChooseDirection;
        this.speed *= 3;
    }

    /**
     * Transitions the ghost out of its reset state
     */
    endReset() {
        this.resetting = false;
        this.baseState = this.direction;
        this.chooseDirection = this.defaultChooseDirection;
        this.speed /= 3;
    }

    /**
     * Selects the next movement direction when the ghost is in either its default or vulnerable
     * states. Somewhat prioritizes movement towards the given target coordinates
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     * @param {number} targetX - The tile map x coordinate that the ghost should try to reach
     * @param {number} targetY - The tile map y coordinate that the ghost should try to reach
     */
    defaultChooseDirection(map, targetX, targetY) {
        // The ghost should always change direction when it's stationary, but only 50% of the time
        // when it moves to a new tile
        if (!this.moving || (this.changedTile && Math.round(Math.random()))) {
            let
                choices = [],
                choice;
        
            // If the ghost is not moving right and there's no barrier to its left
            if (this.direction != RIGHT && map[this.tileY][this.tileX - 1] != 'b') {
                // Left is a valid direction
                choices.push(LEFT);

                // Prioritize this direction if it gets the ghost closer to the target coordinates
                if (targetX < this.tileX) {
                    for (let i = 0; i < GHOST_CHASE_WEIGHT; i++) {
                        choices.push(LEFT);
                    }
                }
            }
            // If the ghost is not moving left and there's no barrier to its right
            if (this.direction != LEFT && map[this.tileY][this.tileX + 1] != 'b') {
                // Right is a valid direction
                choices.push(RIGHT);

                // Prioritize this direction if it gets the ghost closer to the target coordinates
                if (targetX > this.tileX) {
                    for (let i = 0; i < GHOST_CHASE_WEIGHT; i++) {
                        choices.push(RIGHT);
                    }
                }
            }
            // If the ghost is not moving down and there's no barrier above it
            if (this.direction != DOWN && map[this.tileY - 1][this.tileX] != 'b') {
                // Up is a valid direction
                choices.push(UP);

                // Prioritize this direction if it gets the ghost closer to the target coordinates
                if (targetY < this.tileY) {
                    for (let i = 0; i < GHOST_CHASE_WEIGHT; i++) {
                        choices.push(UP);
                    }
                }
            }
            // If the ghost is not moving up and there's no barrier below it
            if (this.direction != UP && map[this.tileY + 1][this.tileX] != 'b') {
                // Down is a valid direction
                choices.push(DOWN);

                // Prioritize this direction if it gets the ghost closer to the target coordinates
                if (targetY > this.tileY) {
                    for (let i = 0; i < GHOST_CHASE_WEIGHT; i++) {
                        choices.push(DOWN);
                    }
                }
            }

            // Randomly select a new direction from the array of valid directions, then queue it
            choice = Math.floor(Math.random() * choices.length);
            this.queueDirection(choices[choice]);
        }
    }

    /**
     * Selects the next movement direction when the ghost is in its reset state. Aggressively
     * prioritizes movement towards the ghost's default tile coordinates
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     */
    resettingChooseDirection(map) {
        // If the ghost's default coordinates have been reached, exit the reset state and skip the
        // rest of the function
        if (this.tileX == this.defaultX && this.tileY == this.defaultY) {
            this.endReset();
            return;
        }

        // The ghost should always change direction when it's stationary and when it moves to a new
        // tile
        if (!this.moving || this.changedTile) {
            let
                choices = [],
                choice;
        
            // If the ghost is not moving right and there's no barrier to its left
            if (this.direction != RIGHT && map[this.tileY][this.tileX - 1] != 'b') {
                // If moving left gets the ghost closer to its default coordinates, immediately
                // queue the direction and skip the rest of the function
                if (this.defaultX < this.tileX) {
                    this.queueDirection(LEFT);
                    return;
                }

                // Left is a valid direction
                choices.push(LEFT);
            }
            // If the ghost is not moving down and there's no barrier above it
            if (this.direction != DOWN && map[this.tileY - 1][this.tileX] != 'b') {
                // If moving up gets the ghost closer to its default coordinates, immediately
                // queue the direction and skip the rest of the function
                if (this.defaultY < this.tileY) {
                    this.queueDirection(UP);
                    return;
                }

                // Up is a valid direction
                choices.push(UP);
            }
            // If the ghost is not moving left and there's no barrier to its right
            if (this.direction != LEFT && map[this.tileY][this.tileX + 1] != 'b') {
                // If moving right gets the ghost closer to its default coordinates, immediately
                // queue the direction and skip the rest of the function
                if (this.defaultX > this.tileX) {
                    this.queueDirection(RIGHT);
                    return;
                }

                // Right is a valid direction
                choices.push(RIGHT);
            }
            // If the ghost is not moving up and there's no barrier below it
            if (this.direction != UP && map[this.tileY + 1][this.tileX] != 'b') {
                // If moving down gets the ghost closer to its default coordinates, immediately
                // queue the direction and skip the rest of the function
                if (this.defaultY > this.tileY) {
                    this.queueDirection(DOWN);
                    return;
                }

                // Down is a valid direction
                choices.push(DOWN);
            }

            // If no direction was immediately queued, but directions are available
            if (choices.length > 0) {
                // Randomly select a new direction from the array of valid directions, then queue it
                choice = Math.floor(Math.random() * choices.length);
                this.queueDirection(choices[choice]);
            }
        }
    }

    /**
     * Updates the ghost's position and animation state
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     * @param {number} elapsed - The time in seconds since the last update
     */
    update(map, elapsed, targetX, targetY) {
        // Superclass update() call
        super.update(map, elapsed);

        // Increment time elapsed since previous animation frame
        this.prevFrame += elapsed;

        // If this animation frame's duration has been reached, move to the next frame
        if (this.prevFrame >= this.frameDur) {
            this.prevFrame -= this.frameDur;
            this.aniState = (this.aniState + 1) % GHOST_FRAMES;
        }

        // Additional logic if the ghost is in a vulnerable blue state
        if (this.blue) {
            // Decrement the blue state timer
            this.blueTimer -= elapsed;

            // If the blue state timer has run out, end the blue state
            if (this.blueTimer <= 0) {
                this.endBlue();
            }
            // Else if fewer than 2 seconds remain on the blue timer, enter the flashing blue state
            else if (this.blueTimer <= 2) {
                this.baseState = GHOST_FLASH_STATE;
            }
        }

        // Choose the next movement direction using the appropriate function
        this.chooseDirection(map, targetX, targetY);
    }

    /**
     * Draws the ghost to a canvas using the given context
     * 
     * @param {CanvasRenderingContext2D} ctx - The context with which to draw the ghost
     */
    draw(ctx) {
        // Source and destination coordinates
        let
            sx = this.aniState * this.size,
            sy = this.baseState * this.size,
            dx = this.x - this.drawOffset,
            dy = this.y - this.drawOffset;

        // Drawing call using the given context
        ctx.drawImage(this.spriteSheet, sx, sy, this.size, this.size,
                                        dx, dy, this.size, this.size);
    }

}