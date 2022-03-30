from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import *

class App(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        dlight = DirectionalLight('dlight')
        dlight.setColor((0.8, 0.8, 0.5, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, -60, 0)
        render.setLight(dlnp)
        alight = AmbientLight('alight')
        alight.setColor((1, 1, 1, 0.125))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        # Load the environment model.
        model = loader.loadModel('models/Ratcoon.bam')
        self.actor = Actor(model, {
            'walk': 'models/Ratcoon_actions.bam',
            'attack': 'models/Ratcoon_actions.bam'
            
        })
        #self.scene = self.loader.loadModel("models/Ratcoon_actions.bam")
        # Reparent the model to render.
        
        
        
        self.actor.loop('walk')

        #self.actor.stop('attack')
        self.actor.reparentTo(self.render)
        print(str(self.actor.get_anim_names()))
        print(str(self.actor.get_current_anim()))
        
        
app = App()
app.run()