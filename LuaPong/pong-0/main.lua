--[[
    Love2d looks for main functions
        it has certain order that the program HAS TO run

]]

-- # global variable configuration/ intialization # --

-- Screen ratio 16:9 ........ remember this ........ --
WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 720

-- Runs when the game first starts up, only once --- only once --

function love.load()
    -- love module's window module's setMode function
    love.window.setMode(WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen = false,
        resizable = false,
        vsync = true
    })

end

function love.update()
end

-- Called after update function by Love2D, this draws what is on your screen --

function love.draw()
    love.graphics.printf(
        'Hello Pong!',          -- text to render
        0,                      -- starting X location
        WINDOW_HEIGHT/2-6,      -- starting Y location
        WINDOW_WIDTH,           -- number of pixels to center within
        'center')               -- center alignment ( also left or right)
end

