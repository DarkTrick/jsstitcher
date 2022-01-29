from ..jsstitcher.main import JsStitcherCUI
import sys

  
def generic_main():
  args = sys.argv[1:]
  JsStitcherCUI().run(args)