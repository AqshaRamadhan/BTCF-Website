import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the old about section and replace it
old_section = '''          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
            <h3>About BTCF</h3>
            <img src="assets/img/about-img-1.jpg" class="img-fluid rounded-4 mb-4" alt="">
            <p><strong>Biodiversity Tourism Center and Fundraising (BTCF)</strong> advances conservation through responsible tourism by protecting biodiversity, empowering communities, and turning high conservation value areas into sustainable destinations. At BTCF, we connect conservation, communities, and responsible tourism to safeguard biodiversity for future generations. Join us in creating measurable impact through research, education, and community-driven conservation</p>
            <p><strong>VISION:</strong> become a leading institution within Universitas Asa Indonesia, internationally recognized for advocating the utilization of High Conservation Value (HCV) areas in oil palm plantations through the development of responsible biodiversity tourism, supporting conservation, community well-being, and long-term sustainability. </p>
          </div>
          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="250">
            <div class="content ps-0 ps-lg-5">
              <p>
                <strong>OUR MISSION</strong>
              </p>
              <ul>
                <li><i class="bi bi-check-circle-fill"></i> <span>To build strategic collaborations between ASAINDO, the oil palm industry, and key stakeholders to advance sustainable biodiversity tourism.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To develop national and international advocacy and partnerships for the responsible utilization of High Conservation Value (HCV) areas.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To mobilize sustainable external funding for applied research, institutional development, and community empowerment.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To strengthen ASAINDO's reputation and visibility at the national and international levels.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To develop adaptive, globally competitive human resources to support biodiversity tourism for the conservation of biodiversity and the well-being of communities.</span></li>
              </ul>
              <p>
                
              </p>

              <div class="position-relative mt-4">
                <img src="assets/img/about-2.jpg" class="img-fluid rounded-4" alt="">
                <a href="https://youtu.be/gRwqy9HKrOE?si=CPxcg1l6WMsXgdKV " class="glightbox pulsating-play-btn"></a>
              </div>
            </div>
          </div>'''

new_section = '''          <div class="col-12" data-aos="fade-up" data-aos-delay="100">
            <h3>About BTCF</h3>
            <img src="assets/img/about-img-1.jpg" class="img-fluid rounded-4 mb-4" alt="">
            <p><strong>Biodiversity Tourism Center and Fundraising (BTCF)</strong> advances conservation through responsible tourism by protecting biodiversity, empowering communities, and turning high conservation value areas into sustainable destinations. At BTCF, we connect conservation, communities, and responsible tourism to safeguard biodiversity for future generations. Join us in creating measurable impact through research, education, and community-driven conservation</p>
          </div>

          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="150">
            <div class="content">
              <h4>Vision</h4>
              <p><strong>VISION:</strong> become a leading institution within Universitas Asa Indonesia, internationally recognized for advocating the utilization of High Conservation Value (HCV) areas in oil palm plantations through the development of responsible biodiversity tourism, supporting conservation, community well-being, and long-term sustainability. </p>
              <div class="position-relative mt-4">
                <img src="assets/img/about-2.jpg" class="img-fluid rounded-4" alt="">
                <a href="https://youtu.be/gRwqy9HKrOE?si=CPxcg1l6WMsXgdKV " class="glightbox pulsating-play-btn"></a>
              </div>
            </div>
          </div>

          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="250">
            <div class="content">
              <h4>Our Mission</h4>
              <ul>
                <li><i class="bi bi-check-circle-fill"></i> <span>To build strategic collaborations between ASAINDO, the oil palm industry, and key stakeholders to advance sustainable biodiversity tourism.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To develop national and international advocacy and partnerships for the responsible utilization of High Conservation Value (HCV) areas.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To mobilize sustainable external funding for applied research, institutional development, and community empowerment.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To strengthen ASAINDO's reputation and visibility at the national and international levels.</span></li>
                <li><i class="bi bi-check-circle-fill"></i> <span>To develop adaptive, globally competitive human resources to support biodiversity tourism for the conservation of biodiversity and the well-being of communities.</span></li>
              </ul>
              <p>
                
              </p>

              <div class="position-relative mt-4">
                <img src="assets/img/about-2.jpg" class="img-fluid rounded-4" alt="">
                <a href="https://youtu.be/gRwqy9HKrOE?si=CPxcg1l6WMsXgdKV " class="glightbox pulsating-play-btn"></a>
              </div>
            </div>
          </div>'''

if old_section in content:
    updated_content = content.replace(old_section, new_section)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("✓ File updated successfully!")
else:
    print("✗ Pattern not found")
