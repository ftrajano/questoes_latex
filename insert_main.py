import os

from conf.db_session import create_session
from models.questao import Questao

DIR_PATH = '/Users/felipe/Public/computacao/app-questoes-latex/questoes/exame12'


def insert_questao() -> None:
	print('Cadastrando questão')
	with create_session() as session:
		for filename in os.listdir(DIR_PATH):
			if filename.endswith('.tex'):
				with open(os.path.join(DIR_PATH, filename), 'r', encoding='utf-8') as file:
					content = file.read()
					# Inserir conteúdo no banco de dados
					questao: Questao = Questao(texto = content)
					session.add(questao)
		session.commit()


if __name__ == '__main__':
	insert_questao()
	