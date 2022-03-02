import { Entity } from './entity.js';
import {
    TILE_SIZE,
    PICKUP_SIZE,
    PICKUP_COLOR,
    PICKUP_VALUE
} from '../constants.js';

/**
 * Represents a pickup entity
 * @class
 */
export class Pickup extends Entity {

    /**
     * Instantiates a new Pickup object
     * 
     * @param {number} tileX - The tile map x coordinate of the entity
     * @param {number} tileY - The tile map y coordinate of the entity
     * @param {string} type - Character representing the pickup type
     */
    constructor(tileX = 1, tileY = 1, type = 'c') {
        // Superclass constructor call
        super(tileX, tileY, PICKUP_SIZE[type]);

        this.type = type;
        this.color = PICKUP_COLOR[type];
        this.value = PICKUP_VALUE[type];
    }

    /**
     * Draws the pickup to a canvas using the given context
     * 
     * @param {CanvasRenderingContext2D} ctx - The context with which to draw the pickup
     */
    draw(ctx) {
        // Drawing calls using the given context
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        ctx.fillStyle = this.color;
        ctx.fill();
    }

    /**
     * Removes the pickup from a canvas using the given context
     * 
     * @param {CanvasRenderingContext2D} ctx - The context with which to remove the pickup
     */
    remove(ctx) {
        let halfTile = TILE_SIZE / 2;

        // Replace the pickup's entire tile with a transparent block
        ctx.clearRect(this.x - halfTile, this.y - halfTile, TILE_SIZE, TILE_SIZE);
    }

}