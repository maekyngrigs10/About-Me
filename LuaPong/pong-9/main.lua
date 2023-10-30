push = require 'push'       --import class
Class = require 'class'
require 'Ball'
require 'paddle'
--screen ratio 16:9............... remember this........
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
--virtual window size: your coordinates will be based on this system
VIRTUAL_WIDTH = 432 
VIRTUAL_HEIGHT = 243
PADDLE_SPEED = 200
--Runs when the game first starts up, only once... only once
function love.load()
    --neares nearest filtering on upscaling and downscaling to prevent blurring of text and graphics 
    love.graphics.setDefaultFilter('nearest','nearest')
    --set the seed or the "randomness" of the serve
    --if we set the "randomness" based on time, in theory it is the most random
    math.randomseed(os.time())
    --more retro looking font we need to load it in
    smallFont = love.graphics.newFont('font.ttf',8)
    scoreFont = love.graphics.newFont('font.ttf',32)
    --set the font to the retro loo
    love.graphics.setFont(smallFont)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })
    --setup player score
    player1Score = 0
    player2Score = 0
    --create a Paddle
    player1 = Paddle(10,30,5,20)
    player2 = Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)
    --create a ball
    ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)
    servingPlayer = 1
    gameState = 'start'
    --initialize our virtual res screen inside of the original window size 
end
--update runs every time the sceen refreshes
function love.update(dt)
    if love.keyboard.isDown('w') then
        player1.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('s') then
        player1.dy = PADDLE_SPEED
    else
        player1.dy=0
    end
    --player 2 or right side movement
    if love.keyboard.isDown('up') then
        player2.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('down') then
        player2.dy = PADDLE_SPEED
    else
        player2.dy=0
    end
    
    if gameState == 'serve' then
        --before switching to play, set the ball's velocity
        if servingPlayer == 1 then
            ball.dx = math.random(140,200)
        else
            ball.dx = -math.random(140,200)
        end
        ball.dy = math.random(-50,50)
    elseif gameState == 'play' then
        if ball:collides(player1) then
            ball.dx = -ball.dx *1.03    --1.03 to speed up
            ball.x = player1.x+5        --to move the ball off of the paddle
            --reset the y velocity
            if ball.dy<0 then
                ball.dy = - math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
        end
        if ball:collides(player2) then
            ball.dx = -ball.dx *1.03    --1.03 to speed up
            ball.x = player2.x-5        --to move the ball off of the paddle
            --reset the y velocity
            if ball.dy<0 then
                ball.dy = - math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
        end
        --wall collision
        if ball.y <=0 then
            ball.y = 0
            ball.dy = -ball.dy
        end
        if ball.y >= VIRTUAL_HEIGHT-4 then
            ball.y = VIRTUAL_HEIGHT-4
            ball.dy = -ball.dy
        end
        --scoring
        if ball.x <0 then
            player2Score = player2Score + 1
            ball:reset()
            gameState = 'serve'
            servingPlayer = 1
        end
        if ball.x >VIRTUAL_WIDTH-4 then
            player1Score = player1Score + 1
            ball:reset()
            gameState = 'serve'
            servingPlayer = 2
        end
        ball:update(dt)
    end
    player1:update(dt)
    player2:update(dt)
end
function love.keypressed(key)
    --keys can be accessed by string name
    if key == 'escape' then
        love.event.quit()
    elseif key == 'enter' or key == 'return' then
        if gameState == 'start' then
            gameState = 'serve'
        elseif gameState == 'serve' then
            gameState ='play'
            --reet the ball and anything else you want to reset...
        end
    end
end
--called after update function by Love2D, this draws what is on your screen
function love.draw()
    --begin rendering a virtual res
    push:apply('start')
    --clear the screen AND set the background color(R,G,B,A)
    love.graphics.clear(40,45,52,255)
    
    love.graphics.setFont(smallFont)
    if gameState == 'start' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'serve' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        -- no UI messages to display in play
    end
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
    player1:render()
    player2:render()
    --ball
    ball:render()
    --end rendering of virtual res
    displayFPS()
    push:apply('end')
end
function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end









