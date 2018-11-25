from bridge_export import bridge_export


map_frames = [
    [
        """ "brg" = 'Brooklyn Bridge' OR "brg" = 'Manhattan Bridge' OR "brg" = 'Williamsburg Bridge' OR "brg" = 'Ed Koch Queensboro Bridge' """,
        "east_river",
    ],
    [
        """ "brg" = 'George Washington Bridge' OR "brg" = 'Lincoln Tunnel' OR "brg" = 'Holland Tunnel' """,
        "hudson_river",
    ],
    [
        """ "brg" = 'Bayonne Bridge' OR "brg" = 'Goethals Bridge' OR "brg" = 'Outerbridge Crossing Bridge' """,
        "staten_island",
    ],
]


bridge_export('config.json', map_frames)