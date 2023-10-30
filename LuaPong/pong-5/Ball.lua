-- dlass Ball:
Ball = Class{}

-- def __init__(self):      Constructor

function Ball:init(x,y,width,height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.dx = math.random(2) == 1 and -100 or 100
    self.dy = math.random(-50,50)

end

-- reset the ball

function Ball:reset()
        -- reset the ball and anything else that you want to reset . . . 
        -- set the ball's default location
        self.x = VIRTUAL_WIDTH/2-2
        self.y = VIRTUAL_HEIGHT/2-2

        -- preset the ball's velocity vector
        self.dx = math.random(2) == 1 and 100 or -100 -- this is how you control who gets the ball served them
        self.dy = math.random(-50,50)*1.5
end

-- update the ball

function Ball:update(dt)
    self.x = self.x +self.dx*dt
    self.y = self.y +self.dy*dt
end

-- draw the ball onto the screen

function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)

end
