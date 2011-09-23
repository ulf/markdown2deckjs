import markdown
from markdown import etree
import sys
from elementtree.ElementTree import Element, SubElement, dump

class SlideProcessor(markdown.treeprocessors.Treeprocessor):
    def create_slide(self, buf, i):
        cont = etree.Element('div')
        cont.set('class', 'slide')
        cont.set('id', str(i))
        i += 1
        for b in buf:
            cont.append(b)
        return cont

    def create_source(self, root):
        if root.tag == 'img' and str(root.get('src'))[:4] == 'http':
            src = etree.Element('cite')
            src.text = 'Quelle: ' + str(root.get('src'))
            src.set('class', 'source')
            root.append(src)
        for c in root:
            c = self.create_source(c)
        return root

    def create_effects(self, root):
        if root.tail and root.tail[-1] == '~':
            root.tail = root.tail[:-1]
            root.set('class', 'slide')
        elif root.text and root.text[-1] == '~':
            root.text = root.text[:-1]
            root.set('class', 'slide')
        for c in root:
            c = self.create_effects(c)
        return root

    def run(self, root):
        root = self.create_source(root)
        root = self.create_effects(root)
        i = 1
        nodes = []
        buf = []
        for c in root:
            if c.tag in ('h1','h2') and len(buf) > 0:
                nodes.append(self.create_slide(buf,i))
                buf = []
                i += 1
            buf.append(c)
        if len(buf) > 0:
            nodes.append(self.create_slide(buf,i))

        slide = etree.Element('div')
        for n in nodes:
            slide.append(n)
        return slide

class slider(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('slideprocessor', SlideProcessor(), '>prettify')
        md.registerExtension(self)

    def reset(self):
        pass


def makeExtension(configs=None) :
    return slider()
