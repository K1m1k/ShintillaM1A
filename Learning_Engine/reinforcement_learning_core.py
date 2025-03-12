import logging
import torch
import torch.nn as nn
import torch.optim as optim

# Configurazione del logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Definizione del Generatore
class Generator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 64),  # Aumentato il numero di neuroni per migliorare la capacità
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_size),
            nn.Tanh()  # Normalizza l'output tra -1 e 1
        )

    def forward(self, x):
        return self.model(x)

# Definizione del Discriminatore
class Discriminator(nn.Module):
    def __init__(self, input_size):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 64),  # Aumentato il numero di neuroni per migliorare la capacità
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()  # Output tra 0 e 1
        )

    def forward(self, x):
        return self.model(x)

# Sistema di Reinforcement Learning con GAN
class ReinforcementLearning:
    def __init__(self, working_memory, long_term_memory, input_size=10, output_size=5):
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory

        # Setup della GAN
        self.generator = Generator(input_size, output_size)
        self.discriminator = Discriminator(output_size)
        self.g_optimizer = optim.Adam(self.generator.parameters(), lr=0.0002)  # Learning rate ridotto per maggiore stabilità
        self.d_optimizer = optim.Adam(self.discriminator.parameters(), lr=0.0002)
        self.criterion = nn.BCELoss()  # Binary Cross-Entropy Loss

        logger.info("GAN inizializzata.")

    def train_gan(self, real_data, num_epochs=100):
        """Addestra la GAN per generare scenari di apprendimento."""
        try:
            batch_size = real_data.size(0)
            logger.info(f"Inizio dell'allenamento della GAN con {num_epochs} epoche...")

            for epoch in range(num_epochs):
                # Crea dati casuali per il generatore
                noise = torch.randn(batch_size, 10)  # Input casuale
                fake_data = self.generator(noise)

                # Allenamento del discriminatore
                real_labels = torch.ones(batch_size, 1)  # Etichette reali (1)
                fake_labels = torch.zeros(batch_size, 1)  # Etichette fake (0)

                self.d_optimizer.zero_grad()
                real_loss = self.criterion(self.discriminator(real_data), real_labels)
                fake_loss = self.criterion(self.discriminator(fake_data.detach()), fake_labels)
                d_loss = real_loss + fake_loss
                d_loss.backward()
                self.d_optimizer.step()

                # Allenamento del generatore
                self.g_optimizer.zero_grad()
                g_loss = self.criterion(self.discriminator(fake_data), real_labels)  # Vuole far passare i fake per reali
                g_loss.backward()
                self.g_optimizer.step()

                # Log delle metriche
                if (epoch + 1) % 10 == 0:
                    logger.info(f"Epoca [{epoch+1}/{num_epochs}] - D Loss: {d_loss.item():.4f}, G Loss: {g_loss.item():.4f}")

        except Exception as e:
            logger.error(f"Errore durante l'allenamento della GAN: {e}")

    def generate_scenario(self):
        """Genera un nuovo scenario di apprendimento per l'agente RL."""
        try:
            noise = torch.randn(1, 10)  # Vettore casuale
            with torch.no_grad():  # Disabilita il calcolo del gradiente
                scenario = self.generator(noise).detach().numpy()
            logger.info(f"Scenario generato: {scenario}")
            return scenario
        except Exception as e:
            logger.error(f"Errore durante la generazione dello scenario: {e}")
            return None

    def save_models(self, generator_path="generator.pth", discriminator_path="discriminator.pth"):
        """Salva i modelli della GAN su disco."""
        try:
            torch.save(self.generator.state_dict(), generator_path)
            torch.save(self.discriminator.state_dict(), discriminator_path)
            logger.info(f"Modelli salvati correttamente: {generator_path}, {discriminator_path}")
        except Exception as e:
            logger.error(f"Errore durante il salvataggio dei modelli: {e}")

    def load_models(self, generator_path="generator.pth", discriminator_path="discriminator.pth"):
        """Carica i modelli della GAN da disco."""
        try:
            self.generator.load_state_dict(torch.load(generator_path))
            self.discriminator.load_state_dict(torch.load(discriminator_path))
            logger.info(f"Modelli caricati correttamente: {generator_path}, {discriminator_path}")
        except Exception as e:
            logger.error(f"Errore durante il caricamento dei modelli: {e}")

    def reward_system(self):
        """Sistema di ricompensa per l'apprendimento."""
        reward = "Ricompensa per l'apprendimento"
        logger.info(f"Ricompensa: {reward}")
        return reward

    def punishment_system(self):
        """Sistema di punizione per l'apprendimento."""
        punishment = "Punizione per l'apprendimento"
        logger.info(f"Punizione: {punishment}")
        return punishment