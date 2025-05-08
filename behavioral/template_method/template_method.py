class Beverage:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Кипятим воду")

    def pour_in_cup(self):
        print("Наливаем в чашку")

    def brew(self):  # Абстрактный шаг
        raise NotImplementedError

    def add_condiments(self):  # Абстрактный шаг
        raise NotImplementedError


class Tea(Beverage):
    def brew(self):
        print("Завариваем чай")

    def add_condiments(self):
        print("Добавляем лимон")


class Coffee(Beverage):
    def brew(self):
        print("Завариваем кофе")

    def add_condiments(self):
        print("Добавляем молоко")


tea = Tea()
tea.prepare()

print("---")

coffee = Coffee()
coffee.prepare()


# ============================

class ReportSender:
    def send_report(self):
        self.prepare()
        self.format()
        self.send()

    def prepare(self):
        print("Собираем данные...")

    def format(self): raise NotImplementedError

    def send(self): raise NotImplementedError


class PDFReportSender(ReportSender):
    def format(self):
        print("Форматируем как PDF")

    def send(self):
        print("Отправляем по email")


class HTMLReportSender(ReportSender):
    def format(self):
        print("Форматируем как HTML")

    def send(self):
        print("Публикуем на сайт")


pdf = PDFReportSender()
pdf.send_report()

print("---")

html = HTMLReportSender()
html.send_report()
