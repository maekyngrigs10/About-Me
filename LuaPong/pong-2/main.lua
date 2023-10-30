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

    -- more retro looking font by loading it in--
    -- var = love.graphics.newFont(FILENAME,fontSize)

    smallFont = love.graphics.newFont('font.ttf',8)

    -- set the font to the retro look --

    love.graphics.setFont(smallFont)

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

    -- clear the screen AND set the background color (R,G,B,A) -- 
    love.graphics.clear(40,45,52,255)

                      -- text to render,starting X location, starting Y location,number of pixels to center within,center alignment ( also left or right)
    love.graphics.printf('Hello Pong!',0,20,VIRTUAL_WIDTH,'center')  

    -- love.graphics.rectangle('fill option',x,y,w,h)

    -- left side paddle
    love.graphics.rectangle('fill',10,30,5,20)

    -- right side paddle
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20)

    -- ball
    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2,VIRTUAL_HEIGHT/2,4,4)

    push:apply('end')
end

