import os

class FindFilesNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "directory": ("STRING", {}),
                "text": ("STRING", {})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "find_files"
    CATEGORY = "custom"

    def find_files(self, directory, text):
        # Verifica se o diretório existe
        if not os.path.isdir(directory):
            return f'O diretório {directory} não existe.'

        found_files = []

        # Percorre todos os arquivos no diretório
        for filename in os.listdir(directory):
            # Verifica se o texto está presente no nome do arquivo
            if text in filename:
                found_files.append(filename)

        # Ordena os arquivos encontrados em ordem crescente
        found_files.sort()

        if found_files:
            # Formata a saída como uma string com os nomes dos arquivos separados por quebra de linha
            files_text = "\n".join(found_files)
            return (files_text,)  # Retorna uma tupla com a string dentro para corresponder ao tipo de retorno definido

        else:
            return (f'Nenhum arquivo encontrado com o texto "{text}".',)  # Retorna uma tupla com a mensagem de erro dentro

# Mapeamento das classes de nós personalizados
NODE_CLASS_MAPPINGS = {
    "FindFilesNode": FindFilesNode
}
