"""
Autonomous Experiment Engine – Central Configuration

This file controls execution behavior, safety policies,
LLM interaction rules, and visualization settings.
Modify ONLY this file to tune system behavior.
"""

# =====================================================
# EXECUTION CONTROL
# =====================================================

MAX_RETRIES = 3
EXECUTION_TIMEOUT_SECONDS = 30


# =====================================================
# DATA POLICY
# =====================================================

# Enforce synthetic data usage only
USE_SYNTHETIC_DATA_ONLY = True


# =====================================================
# SAFETY & SANDBOX CONTROLS
# =====================================================

# Prevent unsafe operations by default
ALLOW_FILE_SYSTEM_ACCESS = False
ALLOW_NETWORK_ACCESS = False


# =====================================================
# LOGGING & OBSERVABILITY
# =====================================================

ENABLE_VERBOSE_LOGS = True


# =====================================================
# LLM BEHAVIOR
# =====================================================

SYSTEM_ROLE = "You are an Autonomous Research Engineer."

LLM_PROVIDER = "groq"
MODEL_NAME = "llama-3.1-70b"

TEMPERATURE = 0.2
MAX_TOKENS = 2048

STRICT_CODE_ONLY_RESPONSE = True


# =====================================================
# VISUALIZATION
# =====================================================

ENABLE_PLOTS = True
DEFAULT_PLOT_BACKEND = "matplotlib"
