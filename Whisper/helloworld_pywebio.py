from pywebio.input import input, FLOAT
from pywebio.output import put_text
import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler

class MainHandler(tornado.web.RequestHandler):
    def get (self):
        self.write('<h1>Hello, world!</h1>')

def bmi():
    height = input("Your Height(cm)：", type=FLOAT)
    weight = input("Your Weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, 'Severely underweight'), (18.4, 'Underweight'),
                  (22.9, 'Normal'), (27.5, 'Overweight'),
                  (40.0, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f, category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    application=tornado.web.Application([
        (r'/', MainHandler),
        (r'/bmi', webio_handler(bmi))
    ])
    application.listen(port=8080,address='localhost')
    tornado.ioloop.IOLoop.current().start()


# pip3 install -U pywebio