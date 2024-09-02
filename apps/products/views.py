from django.shortcuts import render
from django.views import generic
from products.models import Product, Package
from django.templatetags.static import static
from blog.models import Post

# Create your views here.
class ProductDetail(generic.DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        invitations = [
            {
                'name': 'Zaproszenie na wesele',
                'image_path': 'img/invitations/wesele.png',
            },
            {
                'name': 'Zaproszenie na 18stkę',
                'image_path': 'img/invitations/18stka.png',
            },
            {
                'name': 'Zaproszenie na imprezę biznesową',
                'image_path': 'img/invitations/biznes.png',
            },
            {
                'name': 'Zaproszenie na wesele',
                'image_path': 'img/invitations/wesele.png',
            },
            {
                'name': 'Zaproszenie na 18stkę',
                'image_path': 'img/invitations/18stka.png',
            },
            {
                'name': 'Zaproszenie na imprezę biznesową',
                'image_path': 'img/invitations/biznes.png',
            },
        ]
        packages = Package.objects.filter(active=True).order_by('price').all()
        faq_questions = [
            {
                'question': 'Co to jest zaproszenie elektroniczne?',
                'answer': 'Zaproszenie elektroniczne to cyfrowa forma tradycyjnego zaproszenia, która jest wysyłana za pomocą poczty elektronicznej, wiadomości SMS, mediów społecznościowych lub innych platform komunikacyjnych online. Jest to wygodne, szybkie i ekologiczne rozwiązanie dla organizacji różnego rodzaju wydarzeń.'
            },
            {
                'question': 'Jakie są zalety korzystania z zaproszeń elektronicznych?',
                'answer': 'Zaproszenia elektroniczne oferują kilka korzyści, w tym: szybkość wysyłki, ekologię, możliwość personalizacji oraz śledzenie odpowiedzi gości. Dodatkowo, są one bardziej opłacalne w porównaniu do tradycyjnych zaproszeń papierowych.'
            },
            {
                'question': 'Czy mogę personalizować moje zaproszenie elektroniczne?',
                'answer': 'Tak, oferujemy paletę gotowych szablonów zaproszeń. Można je edytować w programach graficznych i wrzucić przerobioną wersję, lub użyć gotowego szablonu.'
            },
            {
                'question': 'Czy zaproszenie elektroniczne można wysłać na różne sposoby?',
                'answer': 'Tak, zaproszenia elektroniczne można wysyłać za pomocą poczty elektronicznej, mediów społecznościowych, aplikacji do komunikacji (np. WhatsApp) lub SMS-a, w zależności od preferencji i dostępnych narzędzi.'
            },
            {
                'question': 'Jakie informacje powinno zawierać zaproszenie elektroniczne?',
                'answer': 'Tutaj panuje pełna dowolność, standardowe zaproszenie elektroniczne powinno zawierać nazwę wydarzenia, datę i godzinę, miejsce, oraz dodatkowe informacje, takie jak instrukcje dojazdu, agenda wydarzenia, oraz możliwość potwierdzenia obecności (RSVP).'
            },
            {
                'question': 'Czy zaproszenia elektroniczne są bezpieczne?',
                'answer': 'Tak, zaproszenia elektroniczne są bezpieczne, stosujemy zaawansowane mechanizmy zabezpieczeń, chroniące dane Twoje i Gości wydarzenia.'
            },
            {
                'question': 'Czy mogę załączyć pliki do mojego zaproszenia elektronicznego?',
                'answer': 'Tak, możesz załączyć całe zaproszenie lub załączyć pliki do szablonu, takie jak zdjęcia, mapy, dokumenty czy inne materiały, które mogą być przydatne dla gości.'
            },
            {
                'question': 'Jakie są koszty związane z wysyłaniem zaproszeń elektronicznych?',
                'answer': 'Koszt zaproszeń elektronicznych zależy od wybranego zakresu funkcji. Niektóre podstawowe opcje są dostępne za darmo, ale za bardziej zaawansowane funkcje mogą być naliczane dodatkowe opłaty.'
            },
            {
                'question': 'Czy mogę śledzić, kto otworzył moje zaproszenie?',
                'answer': 'Tak, oferujemy darmową usługę, która pozwala reagować na zaproszenia i śledzić aktualne odpowiedzi gości wydarzenia.'
            }
        ]
        blog_posts = Post.objects.filter(tag_posts__tag__name=self.object.name).filter(status='published').order_by('-view_count').all()[:3]

        context.update({
            'products': self.get_products(),
            'invitations': invitations,
            'packages': packages,
            'faq_questions': faq_questions,
            'blog_posts': blog_posts
        })


        return context


    def get_products(self):
        return Product.objects.filter(show_on_landing_page=True, active=True)
