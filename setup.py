# ======================================================================
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ======================================================================

import setuptools

def readme() -> str:
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''

setuptools.setup(
	name = 'AFFP',
	version = '0.0.0',
	description = 'Automated Forest Fire Prediction with AI',
	author = 'Valentina Banner, Alicia Yuen, Maya Yan',
	author_email = 'valentinavbanner@gmail.com, yuena945@gmail.com, yanm1@kgv.hk',
	long_description = readme(),
	long_description_content_type = 'text/markdown',
	keywords = 'AI ML NeuralNetwork fire forest environment tensorflow tkinter',
	url = 'https://github.com/realhuman101/AFFP',
	packages = ['src'],
    include_package_data = True,
    python_requires = '>=3.10.0',
	license_file = 'LICENSE',
	license = 'GPL v3',
	install_requires = [
        "tensorflow>=2.10.1",
		"numpy>=1.24.1",
		"pandas>=1.5.2",
		"requests>=2.28.1"
    ],
	entry_points = {
		'gui_scripts': [
			'AFFP = src.gui:start'
		]
	}
)
