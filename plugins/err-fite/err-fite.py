from errbot import BotPlugin, botcmd
from fitedb.fite_client import FiteClient

import ipdb; ipdb.set_trace()
client = FiteClient()
class ErrFite(BotPlugin):
  """
  Conceptual Warfare: Fite!
  """

  @botcmd
  def fite(self, msg, args):
    return "I'm fiting"

  @botcmd
  def get_fites(self, msg, args):
      fites_found = 1


      return "No fites found!"



