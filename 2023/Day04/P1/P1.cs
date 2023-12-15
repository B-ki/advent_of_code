using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace P1
{
	static class Counter
	{
		public static int value;
	}
	class Program
	{
		static void Main()
		{
			string inputFile = "test.txt";
			List<string> lines = File.ReadAllLines(inputFile).ToList();

			List<Card> cards = new List<Card>();

			foreach(string line in lines)
			{
				string[] card_parts = line.Split(':');
				string[] parts = card_parts[1].Split('|');
				string[] winningNumbers = parts[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(num => num.Trim()).ToArray();;
				string[] myNumbers = parts[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(num => num.Trim()).ToArray();

				Card  card = new Card(winningNumbers, myNumbers);
				cards.Add(card);
			}

			int res = 0;

			foreach(Card card in cards)
			{
				Console.WriteLine($"Card {card.Number} : {card.TotPoint}");
				res += card.TotPoint;
			}
			Console.WriteLine($"TOTAL : {res}");
		}
	}

	class Card
	{
		// Class members

		public int Number { get; private set; }
		public string[] WinNumbers { get; private set; }
		public string[] MyNumbers { get; private set; }
		public int TotPoint { get; private set; }

		// Class constructor
		public Card(string[] winningNumbers, string[] myNumbers)
		{
			this.WinNumbers = winningNumbers;
			this.MyNumbers = myNumbers;

			/*
			   Console.WriteLine($"WinNumbers :");
			   foreach(string nb in this.WinNumbers)
			   Console.WriteLine($"nb = {nb}");
			   Console.WriteLine($"MyNumbers :");
			   foreach(string nb in this.MyNumbers)
			   Console.WriteLine($"nb = {nb}");
			   */
			this.TotPoint = 0;
			this.TotPoint = this.CalculatePoints();
			this.Number = Counter.value++;
		}

		// Class function members
		private int CalculatePoints()
		{
			foreach(string number in this.MyNumbers)
			{
				//Console.WriteLine($"My number : {number}");
				if (this.WinNumbers.Contains(number))
				{
					if (this.TotPoint == 0)
					{
						//Console.WriteLine($"TotPoint starting to 1");
						this.TotPoint = 1;
					}
					else
					{
						this.TotPoint *= 2;
						//Console.WriteLine($"TotPoint * 2 = {this.TotPoint}");
					}
				}
			}
			return this.TotPoint;
		}
	}
}
