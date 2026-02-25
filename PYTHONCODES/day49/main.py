from day49.gym_bot import GymBot

if __name__ == "__main__":
    bot = GymBot("noctis@gmail.com", "nocits1234")
    bot.login()
    bot.book_day("Tue")
    bot.book_day("Thu")
    bot.verify_bookings(expected_bookings=2)
