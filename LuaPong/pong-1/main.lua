--[[
    Love2d looks for main functions
        it has certain order that the program HAS TO run

]]

push = require 'push' -- importing class

-- # global variable configuration/ intialization # --

-- Screen ratio 16:9 ........ remember this ........ --

-- physical window --
WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 720

-- virtual window size --> your coordinates will be based on this system --

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

-- Runs when the game first starts up, only once --- only once --

function love.load()
    -- nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics --
    love.graphics.setDefaultFilter('nearest','nearest')
    -- love module's window module's setMode function --
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
      fullscreen = false,
      resizable = false,
      vsync = true
    })

end

function love.update()
end

-- Called after update function by Love2D, this draws what is on your screen --

function love.draw()

    push:apply('start')
                      -- text to render,starting X location, starting Y location,number of pixels to center within,center alignment ( also left or right)
    love.graphics.printf('Hello Pong!',0,VIRTUAL_HEIGHT/2-6,VIRTUAL_WIDTH,'center')  
    
    push:apply('end')
end

