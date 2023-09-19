CODE_DIR=tele_trans
LOCALE=$1
poetry run pybabel init -i ${CODE_DIR}/locales/messages.pot -d ${CODE_DIR}/locales -D messages -l ${LOCALE}