<h1>Kullanılan Araçlar:</h1>
<ol>
<li> Python - Django framework</li>
<li>Docker</li>
<li>Redis->celery işlemlerinin yönetilmesi</li>
<li>Kafkadrop->Django uygulaması için Async işlemlerinin yönetilmesi</li>
<li>PostgreSQL</li>
</ol>

<h1>Endpointler:</h1>
<ol>
<li> Uygulama hazır hale geldiğinde backend localhost 8007 portunda çalışacaktır. Uygulamanın test edilmesi için 
http://localhost:8007/rest/ adresine GET/POST/PUT/DELETE istekleri gönderilebilir.</li>
<li>- İstekler gönderildikten sonra 
http://localhost:8007/rest/report adres
http://localhost:8007/rest/report adresinden son 1 saatteki request'lerin raporuna erişilebilecektir.</li>
<li> Kafka'yı monitor etmek için localhost:9000 portu kullanılabilir.</li>
<li>Uygulamanın ayağa kaldırılması için, proje dizininde docker-compose up --build çalıstırılmalıdır </li>
</ol>

Kod:gAAAAABgUIn3wIfuJEeOoMJLRP_vDzLxvllVh0UhY9QgCRSBspPR0XQQT4XDNMb0EE3CDCFMID2X1hoEv8AaooOUUGVrPEC_7kMLykr3V2nG9_Zwegk-GxLd-OEoI6C6z_zBXUZ5fqJM3uNoEnhQSDTlBGnC76XmqlzZBAAKsn91qDdQaSd1c7WGqptfLsVA9-kmWaq51hNkPm_hbtr3_n3xyvU68Mo56A==

