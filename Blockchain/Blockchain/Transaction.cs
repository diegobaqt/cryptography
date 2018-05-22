using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using NBitcoin;
using QBitNinja.Client;
using QBitNinja.Client.Models;

namespace Blockchain
{
    public class Transaction
    {
        private static QBitNinjaClient _client;
        private static uint256 _transactionId;
        public Transaction()
        {
            var client = new QBitNinjaClient(Network.Main);

            // Parse transaction id to NBitcoin.uint256 so the client can eat it
            var transactionId = uint256.Parse("f13dc48fb035bbf0a6e989a26b3ecb57b84f85e0836e777d6edf60d87a4a2d94");

            _client = client;
            _transactionId = transactionId;
        }

        public void GetTransaction()
        {
            // Query the transaction
            var transactionResponse = _client.GetTransaction(_transactionId).Result;

            var transaction = transactionResponse.Transaction;

            Console.WriteLine("TransactionId: " + transactionResponse.TransactionId); 
            Console.WriteLine("Transaction Hash: " + transaction.GetHash());

            var receivedCoins = transactionResponse.ReceivedCoins;
            foreach (var coin in receivedCoins)
            {
                var amount = (Money) coin.Amount;

                Console.WriteLine("Amount: " + amount.ToDecimal(MoneyUnit.BTC));
                var paymentScript = coin.TxOut.ScriptPubKey;
                Console.WriteLine("Payment Script: " + paymentScript);  // It's the ScriptPubKey
                var address = paymentScript.GetDestinationAddress(Network.Main);
                Console.WriteLine("Address: " + address); // 1HfbwN6Lvma9eDsv7mdwp529tgiyfNr7jc
            }
        }
    }
}
