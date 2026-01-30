function love.load()
    R = 0.3
    G = 0.4
    B = 0.6
    love.graphics.setBackgroundColor(R, G, B)

    player = {
        x = 360,
        y = 360,
        radius = 20,
        speed = 200
    }

    screenWidth = love.graphics.getWidth()
    screenHeight = love.graphics.getHeight()

    rect = {
        x = 45,
        y = 450,
        w = 60,
        h = 25
    }
end

function love.update(dt)
    local oldX, oldY = player.x, player.y

    if love.keyboard.isDown("right") or love.keyboard.isDown("d") then
        player.x = player.x + player.speed * dt
    end
    if love.keyboard.isDown("left") or love.keyboard.isDown("a") then
        player.x = player.x - player.speed * dt
    end
    if love.keyboard.isDown("up") or love.keyboard.isDown("w") then
        player.y = player.y - player.speed * dt
        
    end
    if love.keyboard.isDown("down") or love.keyboard.isDown("s") then
        player.y = player.y + player.speed * dt
    end

    -- Keep player on screen
    player.x = math.max(player.radius, math.min(player.x, screenWidth - player.radius))
    player.y = math.max(player.radius, math.min(player.y, screenHeight - player.radius))

    -- Collision check
    if checkCollision(player.x, player.y, player.radius, rect) then
        -- revert movement on collision
        player.x = oldX
        player.y = oldY
    end
end

function love.draw()
    love.graphics.print("What the...", 300, 500)
    love.graphics.circle("fill", player.x, player.y, player.radius)
    love.graphics.rectangle("fill", rect.x, rect.y, rect.w, rect.h)
end

-- Circle-rectangle collision
function checkCollision(cx, cy, cr, r)
    -- find closest point on rectangle to circle center
    local closestX = math.max(r.x, math.min(cx, r.x + r.w))
    local closestY = math.max(r.y, math.min(cy, r.y + r.h))

    -- distance between closest point and circle center
    local dx = cx - closestX
    local dy = cy - closestY

    return (dx * dx + dy * dy) <= (cr * cr)
end
