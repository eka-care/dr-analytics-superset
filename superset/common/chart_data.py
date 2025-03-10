# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from superset.utils.backports import StrEnum


class ChartDataResultFormat(StrEnum):
    """
    Chart data response format
    """

    CSV = "csv"
    JSON = "json"
    XLSX = "xlsx"
    Email = "email"

    @classmethod
    def table_like(cls) -> set["ChartDataResultFormat"]:
        return {cls.CSV} | {cls.XLSX}

    @classmethod
    def download_like(cls) -> set["ChartDataResultFormat"]:
        return {cls.Email}


class ChartDataResultType(StrEnum):
    """
    Chart data response type
    """

    COLUMNS = "columns"
    FULL = "full"
    QUERY = "query"
    RESULTS = "results"
    SAMPLES = "samples"
    TIMEGRAINS = "timegrains"
    POST_PROCESSED = "post_processed"
    DRILL_DETAIL = "drill_detail"
