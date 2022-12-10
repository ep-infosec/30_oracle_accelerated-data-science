#!/usr/bin/env python
# -*- coding: utf-8 -*--

# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/

import logging

import mlx

logger = logging.getLogger(__name__)

from .mlx_global_explainer import *
from .mlx_local_explainer import *

mlx.initjs()
