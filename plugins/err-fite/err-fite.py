from errbot import BotPlugin, botcmd

class ErrFite(BotPlugin):
  """
  Conceptual Warfare: Fite!
  """

  @botcmd
  def fite(self, msg, args):
    return "I'm fiting"
