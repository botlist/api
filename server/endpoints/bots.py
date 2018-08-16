from api.rest.endpoint import Endpoint
from api.rest.invalidusage import InvalidUsage
from api.rest.response import Response

class RestEndpoint(Endpoint):
    path = '/bots'
    def __init__(self, server):
        super().__init__(server)
    
    async def get(self, request):
        bots = []
        bots.append({
            'id': 408439037771382794,
            'added': None,
            'authors': [],
            'avatar': '97625ffee1fe2921ef8f1a7464f58ebb',
            'discriminator': '9695',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, pro ne rebum sensibus argumentum, brute scripta dolores ius in. No alterum fastidii cotidieque quo, vis graeci invidunt cu, mei ne apeirian menandri. Ei purto wisi virtute has, te tota munere docendi eam. Porro soleat vocent mea ne, eam ea omnis labore molestie. Audiam disputationi id vim, hinc assum an cum.\n\nDebet antiopam gubergren pro ad. Dolor insolens adipisci id mea. Vis et meliore copiosae dissentias. Sumo sententiae vix ex, nibh ubique in duo.\n\nMei id possit quodsi, eu mel denique urbanitas. His aeque minimum intellegam no, no vim dicat mollis disputando. Modus lobortis usu.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'Tanki Online'
        })
        bots.append({
            'id': 477260847786360868,
            'added': None,
            'authors': [
                {
                    'id': 300505364032389122,
                    'username': 'cake',
                    'discriminator': '0001',
                    'avatar': 'a_3181cf136418430fca2ffdde4a04b810'
                }
            ],
            'avatar': None,
            'discriminator': '9696',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, quo ei veri populo meliore, verear accusata eleifend ut quo. Ex quo debitis urbanitas, an luptatum deserunt vis, cu quis alterum duo. No veniam dolore commodo eum. Sit in laoreet percipitur, eos an maiorum convenire complectitur, ea error officiis accusata nam. Cum et graece aliquid adipiscing, pro ad eripuit lobortis intellegam, te meis saperet vis. Cu sea lorem hendrerit, ne adhuc tritani eum.\n\nAd fierent adversarium accommodare cum. Te mel tempor mandamus mediocritatem, sit cibo consulatu at. Ex nec laudem partiendo reprimique, eam erant aperiam tritani et. Est ne facer harum consequuntur, usu ut sumo.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': '50'
        })
        bots.append({
            'id': 338683671664001024,
            'added': None,
            'authors': [],
            'avatar': '7ee41318b1a7c227d5190b969e8c465b',
            'discriminator': '6724',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, mea ad wisi populo semper, in quis graece eum, unum dissentiunt est at. Vel an stet accusamus posidonium. Ex mel mandamus adipiscing, menandri volutpat per at, postea pertinax est ut. Ad alterum insolens interpretaris sea.\n\nSed ei quodsi periculis delicatissimi. Ad erroribus maiestatis definiebas est, no munere assueverit per, vim at duis fuisset scaevola. Nec aliquip molestie ea, per probatus disputando appellantur ne, eos nulla intellegat ei. Assum nostrud duo ex, in eos esse equidem, praesent expetenda an vim.\n\nmittam appetere tincidunt ius eu, ut legere facilis his. Vis vide mundi delenit ut, vim latine.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'Asakura'
        })
        bots.append({
            'id': 361027969570832384,
            'added': None,
            'authors': [],
            'avatar': '2acf69a4516553bee8450916bc9dc434',
            'discriminator': '7407',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, sed id iuvaret habemus, summo periculis explicari vel ne. Ad soleat nullam nonumes has, no usu ridens postulant definitionem. Has quaeque inciderint no, pericula splendide ne vix, ea has modo evertitur. Est cu convenire reformidans, ne nec meliore voluptua temporibus, consequat similique at mea.\n\nAgam consequat scripserit nam at, no sed ridens commodo corpora, veri recusabo dissentiet an pro. Eum primis fastidii adipiscing ad, cu sed noster essent verear, sit an quod omnis moderatius. Accusata conceptam voluptaria at vel, sea ad saepe volutpat, ut sale nostro usu. Ei eam expetenda percipitur, verear abhorreant cotidieque at.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'Bix'
        })
        bots.append({
            'id': 272526395337342977,
            'added': None,
            'authors': [],
            'avatar': '17405bfe32f6d14b97b64538f584dd98',
            'discriminator': '2066',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, omnesque apeirian in eam, meis aliquip omittam ad est. Et eum elit posse ignota. Quod argumentum an eum, ne vero mutat nostro mei, abhorreant deseruisse mnesarchum id vix. Eam aeterno recteque et, vim fastidii percipitur ex, mutat tibique mel ne. An usu iudico temporibus, civibus disputando sed cu.\n\nUt has ferri admodum officiis. At mel magna porro, vim at ludus albucius. Ei eos cibo primis sapientem, usu ut congue vocibus feugait. Mea et duis aeterno denique. Ius at natum integre assentior, an semper abhorreant philosophia qui.\n\nEos ea aeterno prompta volumus, eum atomorum vulputate ut.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'Blizztrack'
        })
        bots.append({
            'id': 446067920070508545,
            'added': None,
            'authors': [],
            'avatar': 'a40ceb675ddf512106ef612b9bd81d2d',
            'discriminator': '6300',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, iriure voluptua indoctum pro ne. Accumsan recteque concludaturque in vim, laudem maluisset vulputate ne sed. Ex vel quot detraxit, lorem dicta solet ut mel. Eu vix lorem novum intellegebat, ad vix idque deserunt gloriatur, ne sea novum veritus percipit.\n\nHas ut commodo oportere assentior dolor.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'Blob Bot'
        })
        bots.append({
            'id': 404762043527462922,
            'added': None,
            'authors': [],
            'avatar': '213c8b555f7cb65b0b284052d12af683',
            'discriminator': '1500',
            'description_long': '',
            'description_short': 'Lorem ipsum dolor sit amet, nec cu euismod reformidans delicatissimi, erat saepe ex mei. Nec regione ceteros ex, nec aliquip voluptatum cu. Ad sed dolores efficiantur, ut facer errem sententiae nam. Nulla nullam laoreet no his. Et postea inimicus intellegam pro, vix ad nonumy petentium. Et paulo quidam vidisse sea.',
            'invite_code': None,
            'picture': None,
            'permissions': 0,
            'servers': 0,
            'upvotes': 0,
            'username': 'BotWorld'
        })
        return Response(200, bots)