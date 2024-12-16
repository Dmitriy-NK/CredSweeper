from pathlib import Path

# total number of files in test samples
SAMPLES_FILES_COUNT = 138

# the lowest value of ML threshold is used to display possible lowest values
NEGLIGIBLE_ML_THRESHOLD = 0.0001

# credentials count after scan with negligible ML threshold
SAMPLES_CRED_COUNT = 425
SAMPLES_CRED_LINE_COUNT = SAMPLES_CRED_COUNT + 19

# Number of filtered credentials with ML
ML_FILTERED = 43

# credentials count after post-processing
SAMPLES_POST_CRED_COUNT = SAMPLES_CRED_COUNT - ML_FILTERED

# with option --doc
SAMPLES_IN_DOC = 468

# archived credentials that are not found without --depth
SAMPLES_IN_DEEP_1 = SAMPLES_POST_CRED_COUNT + 33
SAMPLES_IN_DEEP_2 = SAMPLES_IN_DEEP_1 + 54
SAMPLES_IN_DEEP_3 = SAMPLES_IN_DEEP_2 + 1

# well known string with all latin letters
AZ_DATA = b"The quick brown fox jumps over the lazy dog"
AZ_STRING = AZ_DATA.decode(encoding="ascii")

# tests directory - use ONLY this file relevance for "release_test" workflow
TESTS_PATH = Path(__file__).resolve().parent
# test samples directory
SAMPLES_PATH = TESTS_PATH / "samples"
