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

import pandas as pd

from ..model import datasets 

def test_dataset() -> None:
    testing_data: pd.DataFrame = datasets.testing_data
    training_data: pd.DataFrame = datasets.training_data

    # Check dataset types
    assert isinstance(testing_data, pd.DataFrame)
    assert isinstance(training_data, pd.DataFrame)

    # Check no null
    assert not testing_data.isnull().values.any()
    assert not training_data.isnull().values.any()

    # Check columns
    assert list(testing_data.columns) == ['Temperature', 'RH', 'Ws', 'Rain', 'Classes']
    assert list(training_data.columns) == ['temp', 'RH', 'wind', 'rain', 'area']
