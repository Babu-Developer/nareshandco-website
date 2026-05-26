import sys
from pptx import Presentation
from pptx.util import Pt


def rects_intersect(a, b):
    # a and b are dicts with left, top, width, height
    return not (a['left'] + a['width'] <= b['left'] or
                b['left'] + b['width'] <= a['left'] or
                a['top'] + a['height'] <= b['top'] or
                b['top'] + b['height'] <= a['top'])


def fix_overlaps(prs):
    slide_w = prs.slide_width
    slide_h = prs.slide_height
    for slide in prs.slides:
        # collect modifiable shapes
        rects = []
        for shape in slide.shapes:
            try:
                left = int(shape.left)
                top = int(shape.top)
                width = int(shape.width)
                height = int(shape.height)
            except Exception:
                continue
            rects.append({'shape': shape, 'left': left, 'top': top, 'width': width, 'height': height})

        # sort by top position (higher first)
        rects.sort(key=lambda r: (r['top'], r['left']))

        # simple greedy: for each rect, push any later rects downward if they intersect
        for i in range(len(rects)):
            a = rects[i]
            for j in range(i+1, len(rects)):
                b = rects[j]
                # recompute intersection with updated positions
                if rects_intersect(a, b):
                    # move b down just enough
                    shift = (a['top'] + a['height']) - b['top'] + int(Pt(4))
                    if shift <= 0:
                        shift = int(Pt(4))
                    new_top = b['top'] + shift
                    # don't move beyond slide height
                    if new_top + b['height'] > slide_h:
                        # instead, try moving b up a bit if possible
                        alt_top = a['top'] - b['height'] - int(Pt(4))
                        if alt_top >= 0:
                            new_top = alt_top
                        else:
                            # if can't resolve, try reduce width slightly (best-effort)
                            pass
                    b['top'] = new_top
                    try:
                        b['shape'].top = b['top']
                    except Exception:
                        pass
    return prs


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: fix_overlaps.py input.pptx [output.pptx]')
        sys.exit(2)
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) >= 3 else 'cleaned_' + inp.split('\\')[-1]
    prs = Presentation(inp)
    prs = fix_overlaps(prs)
    prs.save(out)
    print('Saved cleaned file to', out)
