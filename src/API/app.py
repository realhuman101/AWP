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

from flask import Flask
from flask_restful import Api

from endpoints.manual import Manual
from endpoints.future import Future
from endpoints.present import Present

app = Flask(__name__)
api = Api(app)

# Add endpoints
api.add_resource(Manual, '/manual')
api.add_resource(Future, '/future')
api.add_resource(Present, '/present')

def run():
	return app
