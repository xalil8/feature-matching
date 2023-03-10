import os
import shutil

class_names =  ['A-T-bank', 'a101-logo', 'abercrombie-and-fitch', 'abn-amro-bank', 'absa-barclays-africa-group',
 'acrobat', 'adabank-logo', 'adatip', 'adidas', 'adnoc', 'adobe', 'aetna', 'airbnb', 'akbank', 'aktif-bank', 
 'albaraka', 'alibaba', 'alternatif-bank', 'amazon-text', 'american-express', 'american-red-cross', 'anadolu-bank',
  'apple', 'aramco', 'atb-financial', 'axa', 'axisbank', 'banco-do-brasil', 'banco-itau', 'bank-asya', 
  'bank-of-america-logo', 'bank-of-china', 'bank-of-ireland', 'bank-of-montreal', 'barclays', 'better-help-logo', 
  'bfb', 'bim', 'binance-logo', 'box', 'bradesco-text', 'burgan-bank', 'caixa-bank-logo', 'capital-one', 
  'carrefoursa', 'chase', 'chrome-logo', 'citibank', 'coca-cola', 'coinbase', 'comcast', 'countdown', 
  'credit-agricole', 'cvs', 'denizbank-logo', 'denizbank-text', 'desjardins', 'deu-bank', 'dhl', 'dhmi', 
  'diler-bank', 'discover', 'docusign', 'dogan_yatirim_bank', 'dolby', 'drive', 'dropbox', 'e-devlet', 'e-ptt',
  'eba', 'ebay', 'efax', 'emlak-katilim', 'enerjisa', 'enpara', 'equifax', 'facebook-logo', 'facebook-text', 
  'fedex', 'fiba-bank', 'garanti-bbva', 'gmail', 'godaddy', 'golden-global-bank', 'google-logo', 'google-text', 
  'gsd-yatirim-bank', 'habib-bank', 'halkbank-text', 'hangi-kredi', 'hepsiburada-text', 'hollister', 'houseparty',
   'hsbc', 'hsbc-advantage', 'huawei-logo', 'hubspot', 'icbc-bank', 'icici-bank', 'icloud', 'idrive', 
   'iller-bank', 'ingbank', 'instagram-logo', 'instagram-text', 'international-card-service', 'intesa-bank', 
   'intuit', 'isbank', 'istanbul-takasbank', 'itunes', 'jcb-japan', 'jordan', 'jpmorgan-bank', 'kariyer-net', 
   'kayak', 'kuveytturk', 'la-poste', 'linkedin-logo', 'livongo', 'lloyds-bank', 'made-in-china', 'mastercard', 
   'maximum', 'mbna', 'mcafee', 'meb', 'mediamarkt', 'mellat-bank', 'microsoft', 'migros', 'minecraft', 'mufg', 
   'my-ether-wallet', 'mygov-australia', 'n11', 'national-australia-bank', 'netflix', 'nike', 'nurol-yatirim-bank',
    'odeabank', 'oracle', 'orange-telecom', 'outlook', 'papara', 'pasha-bank', 'paya', 'paypal', 'pinterest', 
    'plesk', 'pnc-bank', 'priceline', 'ptt', 'puma', 'qnb-finansbank-logo', 'qnb-finansbank-text', 'rabo-bank', 
    'rakuten', 'ralph-lauren', 'ray-ban', 'ringcentral-logo', 'ringcentral-text', 'roblox', 'royal-bank-of-canada',
     'sagawa', 'sahibinden-logo', 'sahibinden-text', 'salesforce', 'salvation-army-australia', 'sams-club', 
     'samsung', 'santander', 'scotiabank', 'sekerbank', 'sendgrid', 'skype', 'societe-generale-bank', 'sok', 
     'square', 'squarespace', 'standart-chartered-yatirim-bankasi-turk', 'steam', 'stewardship-technology', 
     'stripe', 'suntrust-bank', 'target', 'td-bank', 'teb', 'teknosa', 'teladoc', 'telstra', 'tesco', 
     'the-payment-group', 'thy', 'tinder', 'trendyol', 'turbotax', 'turk-eximbank', 'turkcell', 'turkish-bank', 
     'turkiye-finans-atilim-bankasi', 'turkiye-kalkinma-bankasi', 'turkiye-sinai-kalkinma-bankasi', 
     'turkland-bank', 'turktelekom', 'twilio', 'twitter-logo', 'uber', 'ubs', 'ups', 'us-bank', 'usaa', 
     'vakif-katilim', 'vakifbank', 'visa', 'vodafone', 'walmart', 'whatsapp-logo', 'wilmar', 'woolworths', 
     'world-card', 'xerox', 'xfinity', 'yahoo', 'yapi-kredi-text', 'youtube-logo', 'zara', 'ziraat-katilim-bank',
      'ziraatbank', 'zoom-logo', 'zoom-text']

# Path to the directory containing the pictures
picture_path = "cropped2"


# Path to the directory where the class folders will be created
class_folder_path = "new_classes"

# Loop through the class names
for class_name in class_names:
    # Create a folder with the class name in the class folder path
    class_folder = os.path.join(class_folder_path, class_name)
    os.makedirs(class_folder, exist_ok=True)
    
