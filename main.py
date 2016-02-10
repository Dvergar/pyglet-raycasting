from math import cos, sin, tan, radians, sqrt, pow

import pyglet
from pyglet.gl import *
from pyglet.window import key

bmap = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]


BLOCK_SIZE = 32
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 240


def rotate(v, angle):
    vx = v[0] * cos(radians(-angle)) - v[1] * sin(radians(-angle))
    vy = v[0] * sin(radians(-angle)) + v[1] * cos(radians(-angle))
    return vx, vy


class Game(pyglet.event.EventDispatcher):
    def __init__(self):
        self.window = pyglet.window.Window(
                    vsync=False,
                    width=WINDOW_WIDTH,
                    height=WINDOW_HEIGHT)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.keys)
        self.window.push_handlers(self)
        self.myplayer = Player(self, 100, 200)
        # self.fps = pyglet.clock.ClockDisplay()
        # self.fps.label.x = 200
        pyglet.clock.schedule_interval(self.update, 1 / 60.)

        self.Ax = self.Ay = self.Cx = self.Cy = 0
        self.Bx = self.By = 0
        self.H = self.V = self.C = None
        self.collision_points = {}
        self.map_active = False
        self.rays_angles = []

        angle_range = 60.
        rays = 320
        angle_step = angle_range / rays
        angle = -angle_range / 2
        while angle < angle_range / 2:
            angle += angle_step
            self.rays_angles.append(angle)

        self.img = pyglet.image.load('stone.png')
        self.wall_width = WINDOW_WIDTH / rays
        print "wall width", self.wall_width
        self.wall_tex = self.img.get_texture().id

        ### Blocks instanciation
        for x, row in enumerate(bmap):
            for y, kind in enumerate(row):
                Block(self, x, y, kind)
        print "Game Started"

    def on_key_press(self, symbol, modifiers):
        if symbol == key.F12:
            if self.map_active == False:
                self.map_active = True
            else:
                self.map_active = False

    def update(self, dt):
        self.myplayer.update(dt)

        ### RAAAAYCAAASTIIING
        self.collision_points = {}
        for col, angle in enumerate(self.rays_angles):
            self.collision_points[col] = self.get_collision_point(col, angle)

    def get_collision_point(self, col, angle):
        v = rotate(self.myplayer.v, angle)
        x, y = self.myplayer.x, self.myplayer.y
        dV = dH = 999999  # dummy
        C = None
        angle = radians(90 + angle + self.myplayer.rotation)

        ### A
        if v[1] > 0:
            self.Ay = (y // BLOCK_SIZE) * BLOCK_SIZE + BLOCK_SIZE
        else:
            self.Ay = (y // BLOCK_SIZE) * BLOCK_SIZE - 0.1

        try:
            self.Ax = x + (y - self.Ay) / tan(angle)
        except ZeroDivisionError:
            self.Ax = x

        ### Xa / Ya
        if v[1] > 0:
            try:
                Xa = BLOCK_SIZE / tan(-angle)
            except ZeroDivisionError:
                Xa = 9999
            Ya = BLOCK_SIZE
        else:
            try:
                Xa = BLOCK_SIZE / tan(angle)
            except ZeroDivisionError:
                Xa = 9999
            Ya = -BLOCK_SIZE

        Px = self.Ax
        Py = self.Ay

        ### Horizontal Collisions
        while True:
            self.H = None
            posx = int(Px // BLOCK_SIZE)
            posy = int(Py // BLOCK_SIZE)

            try:
                if Block._registry[(posx, posy)].kind == 1:
                    self.H = (Px, Py)
                    dH = sqrt(pow(self.H[0] - x, 2) + pow(self.H[1] - y, 2))
                    break
                else:
                    Px += Xa
                    Py += Ya
            except KeyError:
                break

        ########################################################

        ### B
        if v[0] > 0:
            self.Bx = (x // BLOCK_SIZE) * BLOCK_SIZE + BLOCK_SIZE
        else:
            self.Bx = (x // BLOCK_SIZE) * BLOCK_SIZE - 0.1

        self.By = y + (x - self.Bx) * tan(angle)

        ### Xa / Ya
        if v[0] > 0:
            Ya = BLOCK_SIZE * tan(-angle)
            Xa = BLOCK_SIZE
        else:
            Ya = BLOCK_SIZE * tan(angle)
            Xa = -BLOCK_SIZE

        Px = self.Bx
        Py = self.By

        ### Vertical Collisions
        while True:
            self.V = None
            posx = int(Px // BLOCK_SIZE)
            posy = int(Py // BLOCK_SIZE)

            try:
                if Block._registry[(posx, posy)].kind == 1:
                    self.V = (Px, Py)
                    dV = sqrt(pow(self.V[0] - x, 2) + pow(self.V[1] - y, 2))
                    break
                else:
                    Px += Xa
                    Py += Ya
            except KeyError:
                break

        if dV < dH:
            C = self.V
            d = dV
            coltype = "V"
        else:
            C = self.H
            d = dH
            coltype = "H"

        offset = x = y = h = sx = sx2 = None  # Ugly but whatever
        if C is not None:
            if coltype == "V":
                offset = C[1] % BLOCK_SIZE
            else:
                offset = C[0] % BLOCK_SIZE

            x = col * self.wall_width
            y = WINDOW_HEIGHT / 2
            h = (BLOCK_SIZE / d) * 277

            k = 1. / BLOCK_SIZE
            sx = offset * k
            sx2 = (offset + self.wall_width) * k

        return C, d, offset, x, y, h, sx, sx2

    def on_draw(self):
        self.window.clear()

        pyglet.gl.glColor3f(0.3, 0.3, 0.3)
        pyglet.gl.glRectf(0, 0,
                            WINDOW_WIDTH, WINDOW_HEIGHT / 2)

        for block in Block._registry.values():
            block.draw()

        self.myplayer.draw()

        if self.map_active:
            # # A Block
            # pyglet.gl.glColor3f(0.6, 0.6, 0.6)
            # x = self.Ax // BLOCK_SIZE
            # y = self.Ay // BLOCK_SIZE
            # x = x * BLOCK_SIZE
            # y = y * BLOCK_SIZE
            # pyglet.gl.glRectf(x, y,
            #             x + BLOCK_SIZE, y + BLOCK_SIZE)

            # # A point
            # pyglet.gl.glColor3f(0.2, 0.2, 1)
            # pyglet.gl.glRectf(self.Ax, self.Ay,
            #                     self.Ax + 2, self.Ay + 2)

            # # B point
            # pyglet.gl.glColor3f(1, 0.1, 1)
            # pyglet.gl.glRectf(self.Bx, self.By,
            #                     self.Bx + 2, self.By + 2)

            # H point
            if self.H is not None:
                pyglet.gl.glColor3f(1, 1, 0.3)
                pyglet.gl.glRectf(self.H[0], self.H[1],
                                    self.H[0] + 2, self.H[1] + 2)

            # V point
            if self.V is not None:
                pyglet.gl.glColor3f(1, 0.3, 1)
                pyglet.gl.glRectf(self.V[0], self.V[1],
                                    self.V[0] + 2, self.V[1] + 2)

            # # C point
            # if self.C is not None:
            #     pyglet.gl.glColor3f(0.1, 1, 0.1)
            #     pyglet.gl.glRectf(self.C[0], self.C[1],
            #                         self.C[0] + 2, self.C[1] + 2)

        for col, (point, d, offset, x, y, h, sx, sx2) \
                    in self.collision_points.items():
            if point is not None:
                if self.map_active:
                    # RAY
                    pyglet.gl.glColor3f(0.6, 0.6, 0.6)
                    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                            ('v2f', (self.myplayer.x, self.myplayer.y,
                                point[0], point[1])))
                    # POINT
                    pyglet.gl.glColor3f(1, 0.1, 0.1)
                    pyglet.gl.glRectf(point[0], point[1],
                                        point[0] + 2, point[1] + 2)

                # WALL
                pyglet.gl.glColor3f(1, 1, 1)
                # pyglet.gl.glColor3f(0.6, 1, 0.3)

                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, self.wall_tex)
                glBegin(GL_QUADS)
                glTexCoord2f(sx, 0.0)
                glVertex2f(x, y - h)
                glTexCoord2f(sx2, 0.0)
                glVertex2f(x + self.wall_width, y - h)
                glTexCoord2f(sx2, 1.0)
                glVertex2f(x + self.wall_width, y + h)
                glTexCoord2f(sx, 1.0)
                glVertex2f(x, y + h)
                glVertex2f(x, y + h)
                glEnd()
                glDisable(GL_TEXTURE_2D)

        # self.fps.draw()


class Block:
    _registry = {}

    def __init__(self, game, posx, posy, kind):
        self.game = game
        self._registry[(posx, posy)] = self
        self.x = posx * BLOCK_SIZE
        self.y = posy * BLOCK_SIZE
        self.posx = posx
        self.posy = posy
        self.kind = kind

    def draw(self):
        if self.game.map_active:
            if self.kind == 0:
                pyglet.gl.glColor3f(0.5, 0.5, 0.5)
            else:
                pyglet.gl.glColor3f(0.5, 0.5, 1)
            pyglet.gl.glRectf(self.x, self.y,
                        self.x + BLOCK_SIZE, self.y + BLOCK_SIZE)

            pyglet.gl.glColor3f(0.4, 0.4, 0.4)
            pyglet.graphics.draw(8, pyglet.gl.GL_LINES,
            ('v2f', (self.x, self.y, self.x, self.y + BLOCK_SIZE,
                self.x, self.y + BLOCK_SIZE, self.x + BLOCK_SIZE, self.y + BLOCK_SIZE,
                self.x + BLOCK_SIZE, self.y + BLOCK_SIZE, self.x + BLOCK_SIZE, self.y,
                self.x + BLOCK_SIZE, self.y, self.x, self.y)
                    ))


class Player:
    SPEED = 400

    def __init__(self, game, x, y):
        self.game = game
        self.x, self.y = x, y
        self.rotation = 0
        self.v = self.vo = (0, 1)

    def update(self, dt):
        if self.game.keys[key.Z]:
            self.x += self.v[0] * self.SPEED * dt
            self.y += self.v[1] * self.SPEED * dt
        if self.game.keys[key.S]:
            self.x -= self.v[0] * self.SPEED * dt
            self.y -= self.v[1] * self.SPEED * dt
        if self.game.keys[key.Q]:
            self.rotation -= 2
            self.v = rotate(self.vo, self.rotation)
        if self.game.keys[key.D]:
            self.rotation += 2
            self.v = rotate(self.vo, self.rotation)

    def draw(self):
        if self.game.map_active:
            # Char
            pyglet.gl.glColor3f(1, 0.5, 0.5)
            pyglet.gl.glRectf(self.x - 2, self.y - 2,
                                self.x + 2, self.y + 2)

            # View ray
            pyglet.gl.glColor3f(0.6, 1, 0.6)
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                    ('v2f', (self.x, self.y,
                        self.x + 100 * self.v[0], self.y + 100 * self.v[1])))

            # View
            pyglet.gl.glColor3f(1, 0.5, 0.5)
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                    ('v2f', (self.x, self.y,
                            self.x + 10 * self.v[0], self.y + 10 * self.v[1])))


if __name__ == '__main__':
    app = Game()
    pyglet.app.run()
