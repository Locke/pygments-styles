from setuptools import setup, find_packages
 
setup (
  name='pygments_styles_locke',
  packages=find_packages(),
  entry_points =
  """
  [pygments.styles]
  default-locke = pygments_styles_locke.styles:DefaultLockeStyle
  """,
)
