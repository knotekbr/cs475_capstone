export const
    GAME_WIDTH = 800,
    GAME_HEIGHT = 620,
    TILE_SIZE = 20,
    TILE_ACTIVE = TILE_SIZE / 2,
    MAP_WIDTH = Math.round(GAME_WIDTH / TILE_SIZE) - 1,
    MAP_HEIGHT = Math.round(GAME_HEIGHT / TILE_SIZE) - 1,
    PICKUP_SIZE = {
        c: 4,
        p: 8
    },
    PICKUP_COLOR = {
        c: 'lightpink',
        p: 'hotpink'
    },
    PICKUP_VALUE = {
        c: 10,
        p: 50
    },
    PLAYER_SPEED = GAME_WIDTH / 6,
    PLAYER_SIZE = 15,
    GHOST_SIZE = 30,
    GHOST_SPEED = GAME_WIDTH / 8,
    GHOST_FRAMES = 10,
    GHOST_FPS = 10,
    GHOST_BLUE_DUR = 6,
    GHOST_BLUE_STATE = 4,
    GHOST_FLASH_STATE = 5,
    GHOST_RESET_STATE = 6,
    GHOST_CHASE_WEIGHT = 5,
    RIGHT = 0,
    DOWN = 1,
    LEFT = 2,
    UP = 3,
    NONE = 4;