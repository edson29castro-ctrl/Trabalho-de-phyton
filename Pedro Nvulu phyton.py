class NascimentoOutubro:
    def __init__(self, id_registo, nome_bebe, genero, nome_mae, medico_responsavel):
        self.id_registo = id_registo
        self.nome_bebe = nome_bebe
        self.genero = genero.strip().capitalize()
        self.nome_mae = nome_mae.strip()
        self.medico_responsavel = medico_responsavel.strip()
        self.mes = "Outubro"

    def __str__(self):
        return (f"ID Registo: {self.id_registo} | Bebé: {self.nome_bebe} | "
                f"Género: {self.genero} | Mãe: {self.nome_mae} | "
                f"Médico: {self.medico_responsavel} | Mês: {self.mes}")


class SistemaNascimentoOutubro:
    def __init__(self):
        self.registos = []
        self.contador_id = 1

    def registar_nascimento(self):
        print("\n--- Novo Registo de Nascimento (Outubro) ---")
        nome_bebe = input("Nome do recém-nascido: ")
        genero = input("Género do bebé (Masculino/Feminino): ")
        nome_mae = input("Nome completo da mãe: ")
        medico = input("Nome do médico responsável pelo parto: ")

        novo_registo = NascimentoOutubro(self.contador_id, nome_bebe, genero, nome_mae, medico)
        self.registos.append(novo_registo)
        print(f"\n[Sucesso] Registo efetuado com ID único atribuído: {self.contador_id}")
        self.contador_id += 1

    def consultar_por_identificador(self):
        print("\n--- Consulta do Registo (Mãe / Identificador) ---")
        termo = input("Introduza o ID do registo ou o nome da mãe: ").strip()

        encontrados = []
        for r in self.registos:
            if termo.isdigit() and int(termo) == r.id_registo:
                encontrados.append(r)
            elif termo.lower() in r.nome_mae.lower():
                encontrados.append(r)

        if encontrados:
            print(f"\nEncontrado(s) {len(encontrados)} registo(s):")
            for r in encontrados:
                print(f" -> ID: {r.id_registo} | Bebé: {r.nome_bebe} | Género: {r.genero} | "
                      f"Mãe: {r.nome_mae} | Médico: {r.medico_responsavel} | Mês: {r.mes}")
        else:
            print("\nNenhum registo encontrado com este identificador ou nome.")

    def consulta_profissional_saude(self):
        print("\n--- Painel Clínico (Profissionais de Saúde) ---")
        if not self.registos:
            print("Não existem registos no sistema.")
            return
        for r in self.registos:
            print(r)

    def estatisticas_outubro(self):
        total = len(self.registos)
        masculino = sum(1 for r in self.registos if r.genero in ["M", "Masculino"])
        feminino = sum(1 for r in self.registos if r.genero in ["F", "Feminino"])

        print("\n--- Relatório e Estatísticas de Outubro ---")
        print(f"Número total de nascimentos em Outubro: {total}")
        print("Distribuição por género:")
        print(f"  - Masculino: {masculino}")
        print(f"  - Feminino: {feminino}")


def main():
    sistema = SistemaNascimentoOutubro()

    while True:
        print("\n==================================================")
        print("       SISTEMA DE NASCIMENTO OUTUBRO (HOSPITAL)   ")
        print("==================================================")
        print("1. Registar novo nascimento")
        print("2. Consultar registo (Mãe / Identificador)")
        print("3. Consultar histórico clínico (Profissionais de Saúde)")
        print("4. Ver estatísticas e total de nascimentos")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            sistema.registar_nascimento()
        elif opcao == "2":
            sistema.consultar_por_identificador()
        elif opcao == "3":
            sistema.consulta_profissional_saude()
        elif opcao == "4":
            sistema.estatisticas_outubro()
        elif opcao == "5":
            print("\nA encerrar o sistema. Até breve!")
            break
        else:
            print("\n[Erro] Opção inválida. Escolha entre 1 e 5.")


if __name__ == "__main__":
    main()