import { Mover } from './mover.js';
import {
    PLAYER_SPEED,
    PLAYER_SIZE
} from '../constants.js';

/**
 * Represents the player entity
 * @class
 */
export class Player extends Mover {

    /**
     * Instantiates a new Player object
     * 
     * @param {number} tileX - The tile map x coordinate of the player
     * @param {number} tileY - The tile map y coordinate of the player
     */
    constructor(tileX, tileY) {
        // Superclass constructor call
        super(tileX, tileY, true, PLAYER_SIZE, PLAYER_SPEED);

        // Current animation state
        this.aniState = 0;
        // Amount by which to increment the animation state with each update
        this.aniInc = 5;

        // Frequently used constants
        this.halfPI = 0.5 * Math.PI;
        this.toRads = Math.PI / 180;
    }

    /**
     * Updates the player's position and animation state
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     * @param {number} elapsed - The time in seconds since the last update
     */
    update(map, elapsed) {
        // Superclass update() call
        super.update(map, elapsed);

        // Only change the animation state if the player is moving
        if (this.moving) {
            // Increment the animation state
            this.aniState += this.aniInc;

            // Invert the animation increment when the animation state reaches a boundary
            if (this.aniState == 0 || this.aniState == 40) {
                this.aniInc *= -1;
            }
        }
    }

    /**
     * Draws the player to a canvas using the given context
     * 
     * @param {CanvasRenderingContext2D} ctx - The context with which to draw the player
     */
    draw(ctx) {
        // Values used to draw Pac-Man, with offset representing the current "size" of his mouth
        // in radians
        let
            offset = this.aniState * this.toRads,
            startAngle = this.direction * this.halfPI + offset,
            endAngle = startAngle + 2 * (Math.PI - offset);

        // Drawing calls using the given context
        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.arc(this.x, this.y, this.size, startAngle, endAngle);
        ctx.lineTo(this.x, this.y);
        ctx.fillStyle = 'yellow';
        ctx.fill();
    }

}