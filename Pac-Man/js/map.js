const
    C = 'c', // Path (coins)
    P = 'p', // Path (power pills)
    O = 'o', // Path (open)
    B = 'b', // Barriers
    S = 's'; // Player start position

/**
 * Represents the game arena as a two dimensional array of characters. Each character represents
 * the contents of a single tile. Allows for collecting pickups and determining valid movements
 * without costly collision detection.
 */
export const map = [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,B,B,B,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,P,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,P,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,C,C,C,C,C,C,B,B,B,C,C,C,C,C,C,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,C,C,C,C,C,C,C,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,C,C,C,C,C,C,C,C,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,B,B,B,O,B,B,B,O,B,B,B,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,C,C,C,C,O,O,O,O,O,O,O,O,O,O,O,O,O,C,P,C,C,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,B,B,B,B,B,B,B,B,B,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,B,B,B,B,O,B,B,B,B,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [O,O,O,O,O,O,O,O,C,C,C,C,C,O,O,B,B,O,O,O,O,O,B,B,O,O,C,C,C,C,C,O,O,O,O,O,O,O,O],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,B,B,B,B,B,B,B,B,B,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,B,B,B,B,B,B,B,B,B,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,O,O,O,O,O,O,O,O,O,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,C,B,B,B,B,B,O,B,B,B,B,B,B,B,B,B,O,B,B,B,B,B,C,B,B,B,B,B,B,B,B],
    [B,C,C,C,C,C,C,C,C,C,C,P,C,C,C,B,B,B,B,B,B,B,B,B,C,C,C,C,C,C,C,C,C,C,C,C,C,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,B,B,C,B,B,B,B,B,B,B,B,B,C,B,B,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,C,B,B,B,B,B,C,B,B,B,B,B,B,B,B,B,C,B,B,B,B,B,C,B,B,B,B,B,B,C,B],
    [B,C,C,C,C,C,B,B,C,C,C,C,C,C,C,C,C,C,C,S,C,C,C,C,C,C,C,C,C,C,C,B,B,C,C,C,C,C,B],
    [B,B,B,B,B,C,B,B,C,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,C,B,B,C,B,B,B,B,B],
    [B,B,B,B,B,C,B,B,C,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,C,B,B,C,B,B,B,B,B],
    [B,C,C,C,C,C,C,C,C,B,B,C,C,C,C,C,C,C,B,B,B,C,C,C,C,C,C,C,B,B,C,C,C,C,C,C,C,C,B],
    [B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B],
    [B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B,B,B,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,B],
    [B,C,C,C,C,C,C,C,P,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,P,C,C,C,C,C,C,C,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
];