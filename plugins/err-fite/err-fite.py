from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
from fitedb.fite_client import FiteClient

from tabulate import tabulate

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
  def current_fite(self, msg, args):
      return client.get_current_fite()

  @botcmd
  def activate_list(self, msg, list_name=None):
      if list_name is not None:
          return client.activate_list(list_name)

  @botcmd
  def deactivate_list(self, msg, args):
      return client.deactivate_list()

  @botcmd
  def public_current(self, msg, args):
      current_list = client.get_current_fite()
      if current_list is None:
          return "No current Fite!"

      headers = ["Fite ID", "Left Fite", "Right Fite"]

      def format_table(fite):
          def fmter(item):
              return "{} ({} votes)".format(item['name'], len(item['votes']))

          return list(map(fmter, fite.values()))

      fites = current_list['fites']

      table = []
      for idx, val in enumerate(fites):
          table.append([idx] + format_table(val))

      return tabulate(list(table), headers, tablefmt="psql")

  @re_botcmd(pattern=r"^vote (\d) (left|right)")
  def vote(self, msg, match):
      return msg.frm
      return client.vote("nick", match.group(1), match.group(2))

  @botcmd
  def clean_db(self, msg, args):
      client.clean_db()

  @botcmd
  def toggle_test(self, msg, args):
      client.reset_for_test()
      return True
