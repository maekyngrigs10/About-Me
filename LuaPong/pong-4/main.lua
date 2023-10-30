--[[
    Love2d looks for main functions
        it has certain order that the program HAS TO run

]]

push = require 'push' -- importing class

-- # global variable configuration/ intialization # --

-- Screen ratio 16:9 ........ remember this ........ --

-- physical window --
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

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

    -- set the seed or the "randomness" of the serve
    -- if we set the "randomness" based on time, in theory it is the most random
    math.randomseed(os.time())

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
    -- set the player scores
        player1Score = 0
        player2Score = 0

    -- set the paddle locations
    player1Y = 30
    player2Y = VIRTUAL_HEIGHT-50

    -- set the ball's default location
    ballX = VIRTUAL_WIDTH/2-2
    ballY = VIRTUAL_HEIGHT/2-2

    -- preset the ball's velocity vector
    ballDX = math.random(2) == 1 and 100 or -100 -- this is how you control who gets the ball served them
    ballDY = math.random(-50,50)

    -- setting up the game to be in a "start mode" or "main menu"
    gameState = 'start'
    

end

function love.update(dt)
    -- update runs everytime the screen refreshes --

    -- player 1/left side movement (the variable) -- 

    if love.keyboard.isDown('w') then
        player1Y = player1Y + -PADDLE_SPEED*dt
        player1Y = math.max(0,player1Y + -PADDLE_SPEED*dt)
    elseif love.keyboard.isDown('s') then
        player1Y = player1Y + PADDLE_SPEED*dt
        player1Y = math.min(VIRTUAL_HEIGHT - 20,player1Y+PADDLE_SPEED*dt)
    end

    -- player 2/ right side movement --

    if love.keyboard.isDown('up') then
        player2Y = player2Y + -PADDLE_SPEED*dt
        player2Y = math.max(0,player2Y+-PADDLE_SPEED*dt)
    elseif love.keyboard.isDown('down') then
        player2Y = player2Y + PADDLE_SPEED*dt
        player2Y = math.min(VIRTUAL_HEIGHT-20,player2Y+PADDLE_SPEED*dt)
    end

    -- pos = init pos + vector * time -- kinematics -- physics

    if gameState == 'play' then
        ballX = ballX+ballDX*dt
        ballY = ballY+ballDY*dt
    end
end

function love.keypressed(key)
    -- keys can be accessed by strong name --

    if key == 'escape' then
        love.event.quit()
    elseif key == 'enter' or key == 'return' then
        if gameState == 'start' then
            gameState = 'play'
        else
            gameState ='start'

            -- reset the ball and anything else that you want to reset . . . 
            -- set the ball's default location
            ballX = VIRTUAL_WIDTH/2-2
            ballY = VIRTUAL_HEIGHT/2-2

            -- preset the ball's velocity vector
            ballDX = math.random(2) == 1 and 100 or -100 -- this is how you control who gets the ball served them
            ballDY = math.random(-50,50)
        end
    end
end

-- Called after update function by Love2D, this draws what is on your screen --

function love.draw()

    push:apply('start')

    -- clear the screen AND set the background color (R,G,B,A) -- 
    love.graphics.clear(40,45,52,255)
    love.graphics.setFont(smallFont)

    if gameState == 'start' then
                        -- text to render,starting X location, starting Y location,number of pixels to center within,center alignment ( also left or right)
        love.graphics.printf('Hello Start State!',0,20,VIRTUAL_WIDTH,'center')
    else 
        love.graphics.printf('Hello Play State!',0,20,VIRTUAL_WIDTH,'center')
    end 
    
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)

    -- love.graphics.rectangle('fill option',x,y,w,h)

    -- left side paddle
    love.graphics.rectangle('fill',10,player1Y,5,20)

    -- right side paddle
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)

    -- ball
    love.graphics.rectangle('fill',ballX,ballY,4,4)

    push:apply('end')
end

