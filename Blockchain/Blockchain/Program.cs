using System;
using NBitcoin;

namespace Blockchain
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create private Key
            var privateKey = new Key();

            // Genera la llave pública a partir de la llave privada
            var publicKey = privateKey.PubKey;
            Console.WriteLine("Public Key: " + publicKey);

            var publicKeyHash = publicKey.Hash;
            Console.WriteLine("Public Key Hash: " + publicKeyHash);

            // Red de Bitcoin que todos utilizan.
            var mainNetAddress = publicKeyHash.GetAddress(Network.Main);
            Console.WriteLine("Address (Bitcoin Network): " + mainNetAddress);

            // Red de Bitcoin para propósito de desarrollo. Los Bitcoins en esta red no valen nada.
            var testNetAddress = publicKeyHash.GetAddress(Network.TestNet);
            Console.WriteLine("Address (Bitcoin Network for Development): " + testNetAddress);

            // Es un pequeño script que explica qué condiciones se deben cumplir para reclamar 
            // la propiedad de bitcoins.
            Console.WriteLine("ScriptPubKey (BN): " + mainNetAddress.ScriptPubKey); 
            Console.WriteLine("ScriptPubKey (BND): " + testNetAddress.ScriptPubKey);

            // Genera nuestro Bitcoin secret (también conocido como Wallet Import Format o simplemente WIF) 
            // desde nuestra llave privada para la red principal.
            var mainNetPrivateKey = privateKey.GetBitcoinSecret(Network.Main);
            Console.WriteLine("WIF (Main Network): " + mainNetPrivateKey);
            
            var transaction = new Transaction();
            transaction.GetTransaction();
        }
    }
}
