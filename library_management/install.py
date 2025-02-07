import frappe

def after_install():
    insert_articles()

def insert_articles():
    articles = [{
        "name":"A lei da atra\u00e7\u00e3o",
        "article_name":"A lei da atra\u00e7\u00e3o",
        "author":"Michael J. Losier",
        "isbn":"8544106358",
        "publisher":"LeYa",
        "status":"Issued",
        "description":"<div class=\"ql-editor read-mode\"><p>Best-seller em mais de 20 pa\u00edses, A Lei da Atra\u00e7\u00e3o, que j\u00e1 vendeu milh\u00f5es exemplares no mundo todo, nos ensina como atrair mais daquilo que desejamos Em alguns momentos, algo que desejamos muito parece acontecer subitamente, como que por coincid\u00eancia. Noutros momentos, algo que tememos muito tamb\u00e9m parece se manifestar como que por coincid\u00eancia. Experi\u00eancias como essas evidenciam a exist\u00eancia de uma for\u00e7a muito poderosa chamada de \u201cLei da Atra\u00e7\u00e3o\u201d, que \u00e9 a capacidade que temos de, com nossos pensamentos e emo\u00e7\u00f5es, criar a realidade em que vivemos. A Lei da Atra\u00e7\u00e3o: O segredo, de Rhonda Byrne, colocado em pr\u00e1tica explica como podemos utilizar essa \u201clei\u201d sempre a nosso favor e traz exerc\u00edcios simples e dicas \u00fateis que nos ajudam a integrar seus princ\u00edpios \u00e0 nossa vida cotidiana para atrair mais do que queremos e afastar o que n\u00e3o nos serve. A partir de tr\u00eas passos muito f\u00e1ceis de seguir, este livro nos ajudar\u00e1 a alcan\u00e7ar objetivos como: encontrar o parceiro ideal para relacionamentos duradouros, aumentar o nosso ganho financeiro, crescer na carreira profissional, empreender novos neg\u00f3cios e construir a vida com que sempre sonhamos. Sobre o autor: Michael J. Losier \u00e9 psic\u00f3logo e come\u00e7ou a estudar programa\u00e7\u00e3o neurolingu\u00edstica na d\u00e9cada 1990. No ano 2000, conheceu a Lei da Atra\u00e7\u00e3o e levou esse conhecimento para o seu trabalho, alcan\u00e7ando resultados surpreendentes. A Lei da Atra\u00e7\u00e3o: o Segredo, de Rhonda Byrne, colocado em pr\u00e1tica foi lan\u00e7ado em 2004 numa edi\u00e7\u00e3o independente nos Estados Unidos, mas alcan\u00e7ou um enorme sucesso no boca a boca entre os leitores e chegou aos primeiros lugares das listas de mais vendidos. J\u00e1 publicado em mais de 20 pa\u00edses, A Lei da Atra\u00e7\u00e3o \u00e9 um sucesso absoluto no Brasil.</p></div>",
        "published":1
    },{
        "name":"Pense & enrique\u00e7a",
        "article_name":"Pense & enrique\u00e7a",
        "author":"Napoleon Hill",
        "isbn":"8546501467",
        "publisher":"BestSeller",
        "status":"Available",
        "description":"<div class=\"ql-editor read-mode\"><p>Investigando a vida de diversos milion\u00e1rios da hist\u00f3ria dos Estados Unidos, como Thomas Edison, Henry Ford e Theodore Roosevelt, Napoleon Hill descobriu um segredo que poucos tinham desvendado: o que esses homens t\u00eam em comum que os fizeram ser t\u00e3o bem-sucedidos?</p><p><br></p><p>Pense &amp; enrique\u00e7a revela os segredos da fortuna dos maiores milion\u00e1rios dos Estados Unidos. A partir de um programa de 13 passos, Napoleon Hill mostra o caminho certo para a riqueza e a felicidade.</p><p><br></p><p>Neste livro, Hill prop\u00f5e a seguinte quest\u00e3o: \u201cComo vencer na vida?\u201d</p><p><br></p><p>Por mais de vinte anos analisando a carreira dos homens mais ricos da hist\u00f3ria dos Estados Unidos e, com base na experi\u00eancia deles, descobriu o segredo para gerar riqueza. </p><p><br></p><p>Sucesso absoluto desde sua primeira edi\u00e7\u00e3o, em 1937, este livro continua a encantar e a ensinar todos aqueles que t\u00eam interesse em tirar vantagem do crescimento econ\u00f4mico, provando que a f\u00f3rmula para ganhar dinheiro nunca muda.</p><p><br></p><p>Prepare-se para ter sua realidade transformada pela filosofia de Napoleon Hill, que o ajudar\u00e1 a ter mais facilidade em negocia\u00e7\u00f5es e a obter o poder de enriquecer a sua vida!</p></div>",
        "published":0
    }]

    for article in articles:
        if not frappe.db.exists("Article", article["name"]):
            doc = frappe.new_doc("Article")
            for key in article:
                doc.set(key, article[key])
            doc.insert(ignore_permissions=True)
