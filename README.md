# Learn-Ros2
Projetos de estudo sobre Ros2 utilizando Python e C++

São o Mesmo Projeto porem em em C++ e outro em Python

## Publisher e Subscriber

### Publisher:

Um Publisher em ROS 2 desempenha o papel de um nó responsável por enviar mensagens para um tópico específico no sistema. Em termos simples, podemos pensar em um Publisher como um produtor de dados que compartilha informações com outros componentes do sistema ROS 2. Aqui estão alguns pontos essenciais sobre Publishers:

Envio de Mensagens: Um Publisher envia mensagens estruturadas, que podem conter informações como dados de sensores, comandos de controle, estados do robô, entre outros. Por exemplo, um nó de sensor de velocidade pode publicar a velocidade atual do robô no tópico "/robot/speed".

Definição de Tópico: As mensagens são publicadas em tópicos específicos. Um tópico é um canal de comunicação nomeado dentro do sistema ROS 2, permitindo que múltiplos nós publiquem e/ou se inscrevam para receber mensagens relevantes para suas funcionalidades.

Arquitetura Distribuída: Publishers podem estar localizados em nós (processos) diferentes ou no mesmo nó, dependendo da arquitetura do sistema. Isso permite que diferentes partes do sistema robótico se comuniquem eficientemente, promovendo a modularidade e a escalabilidade.

Assincronicidade: A comunicação entre Publishers e Subscribers é assíncrona, o que significa que os nós podem operar independentemente uns dos outros. Isso é crucial em sistemas robóticos onde o tempo de resposta é crítico e várias tarefas precisam ser executadas simultaneamente.

Flexibilidade e Reutilização: Utilizando tópicos, os desenvolvedores podem projetar sistemas modulares onde diferentes componentes podem ser substituídos ou atualizados independentemente. Isso promove a reutilização de código e facilita a manutenção do sistema.

### Subscriber:

Um Subscriber em ROS 2 é um nó que se inscreve em um tópico específico para receber e processar mensagens publicadas por Publishers. Funciona como um consumidor de dados que utiliza as informações recebidas para realizar ações específicas ou tomar decisões dentro do sistema. Aqui estão os pontos principais sobre Subscribers:

Recepção de Mensagens: O Subscriber monitora um tópico específico e recebe ativamente as mensagens que são publicadas nesse tópico por um ou mais Publishers. Por exemplo, um nó responsável pelo controle do robô pode se inscrever no tópico "/robot/speed" para receber e interpretar comandos de velocidade.

Processamento de Dados: Após receber uma mensagem, o Subscriber pode processar os dados contidos nela para executar operações como controle de atuadores, planejamento de movimento, geração de mapas, entre outros. A capacidade de processamento de dados em tempo real é fundamental para sistemas robóticos autônomos.

Sincronização e Atualizações: Subscribers podem ser configurados para operar de maneira sincronizada ou assíncrona com o envio de mensagens pelos Publishers, dependendo dos requisitos do sistema. Isso garante que as atualizações de estado e os comandos sejam processados de maneira oportuna e precisa.

Integração com ROS 2: O framework ROS 2 facilita a configuração e operação de Subscribers através de uma API robusta e documentada. Desenvolvedores podem implementar Subscribers em diferentes linguagens de programação suportadas por ROS 2, como C++, Python, e outras, garantindo flexibilidade e interoperabilidade.

#### Funcionamento Conjunto:

A interação entre Publishers e Subscribers forma a espinha dorsal da comunicação em sistemas robóticos baseados em ROS 2. Aqui estão alguns aspectos chave do funcionamento conjunto:

Troca de Informações: Publishers e Subscribers trabalham em conjunto para trocar informações críticas em tempo real, permitindo que o sistema robótico funcione de maneira coordenada e responsiva.

Gerenciamento de Tópicos: O gerenciamento eficaz de tópicos dentro do ecossistema ROS 2 facilita a comunicação entre múltiplos nós, promovendo a modularidade e a expansibilidade do sistema.

Escalabilidade: A arquitetura distribuída de ROS 2 permite que Publishers e Subscribers sejam distribuídos em diferentes nós, suportando sistemas complexos e distribuídos que são comuns em aplicações robóticas avançadas.

Monitoramento e Depuração: Ferramentas integradas de monitoramento e depuração em ROS 2 facilitam a verificação do fluxo de mensagens entre Publishers e Subscribers, garantindo a confiabilidade e o desempenho do sistema.
