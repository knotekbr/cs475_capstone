import { Entity } from './entity.js';
import {
    MAP_WIDTH,
    TILE_SIZE,
    TILE_ACTIVE,
    LEFT,
    NONE
} from '../constants.js';

/**
 * Represents a moving entity
 * @class
 */
export class Mover extends Entity {

    /**
     * Instantiates a new Mover object
     * 
     * @param {number} tileX - The tile map x coordinate of the entity
     * @param {number} tileY - The tile map y coordinate of the entity
     * @param {number} size - The size of the entity
     * @param {number} speed - The speed of the entity
     * @param {number} direction - The starting direction of the entity
     */
    constructor(tileX, tileY, isPlayer, size, speed = 0, direction = LEFT) {
        // Superclass constructor call
        super(tileX, tileY, size);

        this.isPlayer = isPlayer;
        this.speed = speed;
        this.moving = false;
        // Number of pixels moved from center of current tile, used to update tileX and tileY
        this.moved = 0;

        // Speed multipliers for each axis whose indices correspond to a direction value
        // [RIGHT, DOWN, LEFT, UP, NONE]
        this.xMults = [1, 0, -1, 0, 0];
        this.yMults = [0, 1, 0, -1, 0];

        // Current direction and corresponding speed multipliers
        this.direction = NONE;
        this.xMult = 0;
        this.yMult = 0;

        // Next direction and corresponding speed multipliers
        this.nextDirection = direction;
        this.nextXMult = this.xMults[direction];
        this.nextYMult = this.yMults[direction];

        // Set to true if the entity has moved to a new tile during an update
        this.changedTile = false;
    }

    /**
     * Queues the entity's next movement direction
     * 
     * @param {number} direction - The desired direction
     */
    queueDirection(direction) {
        // Short circuit if the given direction is the current direction or is already queued
        if (direction == this.direction || direction == this.nextDirection) { return; }

        // Store the given direction and corresponding speed multipliers
        this.nextDirection = direction;
        this.nextXMult = this.xMults[direction];
        this.nextYMult = this.yMults[direction];

        // If the given direction is the opposite of the current direction, there is no need to
        // wait. Change direction immediately
        if (Math.abs(this.nextDirection - this.direction) == 2) {
            // Treat the next tile as the starting point for this direction change
            this.tileX += this.xMult;
            this.tileY += this.yMult;
            // Adjust moved to account for the tile change
            this.moved = TILE_SIZE - this.moved;

            this.changeDirection();
        }
    }

    /**
     * Changes the entity's movement direction to the queued direction
     */
    changeDirection() {
        // Set moving to true in case the entity is currently stationary
        this.moving = true;
        // Set direction and speed multipliers to their queued counterparts
        this.direction = this.nextDirection;
        this.xMult = this.nextXMult;
        this.yMult = this.nextYMult;

        // Set queued direction and speed multipliers to default values
        this.nextDirection = NONE;
        this.nextXMult = 0;
        this.nextYMult = 0;
    }

    /**
     * If enough movement has occurred, updates the entity's tileX or tileY coordinate and checks
     * to see if movement should stop
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     */
    updateTile(map) {
        if (this.moved >= TILE_SIZE) {
            this.changedTile = true;
            // Increment tileX or tileY in the direction of movement
            this.tileX += this.xMult;
            this.tileY += this.yMult;
            // Offset moved to track movement from the new tile
            this.moved -= TILE_SIZE;

            // Stop moving if the next tile in the direction of movement is a barrier
            if (map[this.tileY + this.yMult][this.tileX + this.xMult] == 'b') {
                // Center the entity on the current tile
                this.x = (this.tileX + 1) * TILE_SIZE;
                this.y = (this.tileY + 1) * TILE_SIZE;

                // Stop moving and reset movement tracker
                this.moving = false;
                this.moved = 0;
            }
        }
    }

    /**
     * Updates the entity's position
     * 
     * @param {(string|number)[][]} map - Two-dimensional array representing the game arena
     * @param {number} elapsed - The time in seconds since the last update
     */
    update(map, elapsed) {
        this.changedTile = false;

        // Only perform position calculations if the entity is moving
        if (this.moving) {
            // The number of pixels moved in this update
            let movement = this.speed * elapsed;

            // Increment the entity's position in the direction of movement
            this.x += movement * this.xMult;
            this.y += movement * this.yMult;

            // Track how much movement has occurred
            this.moved += movement;

            // Update tileX or tileY if necessary
            this.updateTile(map);

            // If the entity has moved off of the map to the left, "teleport" it to the right side
            // of the map
            if (this.tileX < 0) {
                this.tileX = MAP_WIDTH - 1;
                this.x = this.x = (this.tileX + 1) * TILE_SIZE;
                this.moved = 0;
            }
            // Else if the entity has moved off of the map to the right, "teleport" it to the left
            // side of the map
            else if (this.tileX >= MAP_WIDTH) {
                this.tileX = 0;
                this.x = this.x = (this.tileX + 1) * TILE_SIZE;
                this.moved = 0;
            }
        }

        // If a movement direction is queued and the entity is near the center of the current tile
        if (this.nextDirection != NONE && this.moved <= TILE_ACTIVE) {
            // Change directions if the tile in the next direction is not a barrier
            if (map[this.tileY + this.nextYMult][this.tileX + this.nextXMult] != 'b') {
                // Center the entity on the current tile and reset movement tracker
                this.x = (this.tileX + 1) * TILE_SIZE;
                this.y = (this.tileY + 1) * TILE_SIZE;
                this.moved = 0;

                this.changeDirection();
            }
        }
    }

}