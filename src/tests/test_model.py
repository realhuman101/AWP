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
    dataset: pd.DataFrame = datasets.dataset

    # Check dataset types
    assert isinstance(dataset, pd.DataFrame)

    # Check no null
    assert not dataset.isnull().values.any()

    # Check columns
    assert list(dataset.columns) == ['Temperature', 'RH', 'Ws', 'Rain', 'Classes']
