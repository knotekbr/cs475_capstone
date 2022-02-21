import { TILE_SIZE } from '../constants.js';

/**
 * Represents a game entity
 * @class
 */
export class Entity {

    /**
     * Instantiates a new Entity object
     * 
     * @param {number} tileX - The tile map x coordinate of the entity
     * @param {number} tileY - The tile map y coordinate of the entity
     * @param {number} size - The size of this entity
     */
    constructor(tileX = 1, tileY = 1, size = 5) {
        this.size = size;
        this.tileX = tileX;
        this.tileY = tileY;

        // Calculate actual x and y coordinates based on tile coordinates
        this.x = (tileX + 1) * TILE_SIZE;
        this.y = (tileY + 1) * TILE_SIZE;
    }

}