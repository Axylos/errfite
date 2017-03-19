from errbot import BotPlugin, botcmd, arg_botcmd
from fitedb.fite_client import FiteClient

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
      fites = client.get_all_fites()

      if fites:
          return fites
      else:
          return "No fites found!"

  @botcmd
  def new_fitelist(self, msg, new_list=None):

      client.new_fitelist(new_list)
      return 'Fite Created'


  @botcmd
  def get_fitelist(self, msg, list_name=None):
      if list_name is not None:
          fitelist = client.fetch_fitelist(list_name)
          if not fitelist:
              return "No Fites Found!"
          else:
              return fitelist.dump()

  @arg_botcmd('right_fite', type=str)
  @arg_botcmd('left_fite', type=str)
  @arg_botcmd('list_name', type=str)
  def add_fite(self, msg, list_name=None, left_fite=None, right_fite=None):
      print("hey there")
      print(list_name, left_fite, right_fite)
      return client.add_fite(list_name, (left_fite, right_fite))

  @botcmd
  def clean_db(self, msg, args):
      client.clean_db()

  @botcmd
  def toggle_test(self, msg, args):
      client.reset_for_test()
      return True
