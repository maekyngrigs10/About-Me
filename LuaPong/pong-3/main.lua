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

PADDLE_SPEED = 200

player1Y = 30
player1Score = 0

player2Y = VIRTUAL_HEIGHT-50
player2Score = 0

-- Runs when the game first starts up, only once --- only once --

function love.load()
    -- nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics --

    love.graphics.setDefaultFilter('nearest','nearest')

    -- more retro looking font by loading it in--
    -- var = love.graphics.newFont(FILENAME,fontSize)

    smallFont = love.graphics.newFont('font.ttf',8)

    -- set the font to the retro look --

    love.graphics.setFont(smallFont)

    scoreFont = love.graphics.newFont('font.ttf',32)

    -- love module's window module's setMode function --

    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
      fullscreen = false,
      resizable = false,
      vsync = true
})

    -- paddle locations
    player1Y = 30
    player2Y = VIRTUAL_HEIGHT-50

    -- player scores
    player1Score = 0
    player2Score = 0
    

end

function love.update(dt)
    -- update runs everytime the screen refreshes --

    -- player 1/left side movement (the variable) -- 

    if love.keyboard.isDown('w') then
        player1Y = player1Y + -PADDLE_SPEED*dt
    elseif love.keyboard.isDown('s') then
        player1Y = player1Y + PADDLE_SPEED*dt
    end

    -- player 2/ right side movement --

    if love.keyboard.isDown('up') then
        player2Y = player2Y + -PADDLE_SPEED*dt
    elseif love.keyboard.isDown('down') then
        player2Y = player2Y + PADDLE_SPEED*dt
    end

end

function love.keypressed(key)
    -- keys can be accessed by strong name --

    if key == 'escape' then
        love.event.quit()
    end
end

-- Called after update function by Love2D, this draws what is on your screen --

function love.draw()

    push:apply('start')

    -- clear the screen AND set the background color (R,G,B,A) -- 
    love.graphics.clear(40,45,52,255)
    love.graphics.setFont(smallFont)
                      -- text to render,starting X location, starting Y location,number of pixels to center within,center alignment ( also left or right)
    love.graphics.printf('Hello Pong!',0,20,VIRTUAL_WIDTH,'center') 
    
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)

    -- love.graphics.rectangle('fill option',x,y,w,h)

    -- left side paddle
    love.graphics.rectangle('fill',10,player1Y,5,20)

    -- right side paddle
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)

    -- ball
    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2,VIRTUAL_HEIGHT/2,4,4)

    push:apply('end')
end

